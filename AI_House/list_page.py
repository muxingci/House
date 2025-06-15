from flask import Blueprint, request, render_template, url_for, redirect
from models import House
import math

# 创建蓝图对象
list_page = Blueprint('list_page', __name__)

# 实现搜索列表页的功能
@list_page.route('/query')
def search_txt_info():
    # 获取地区字段的查询
    if request.args.get('addr'):
        addr = request.args.get('addr')
        result = House.query.filter(House.address == addr).order_by(House.publish_time.desc()).all()
        return render_template('search_list.html', house_list=result)

    # 获取户型字段的查询
    if request.args.get('rooms'):
        rooms_info = request.args.get('rooms')
        result = House.query.filter(House.rooms == rooms_info).order_by(House.publish_time.desc()).all()
        return render_template('search_list.html', house_list=result)
    return redirect(url_for('index_page.index'))


# 最新房源列表页展示的功能
@list_page.route('/list/pattern/<int:page>')
def return_new_list(page):
    # 获取房源总数量
    house_num = House.query.count()
    # 计算总的页码数，向上取整
    total_num = math.ceil(house_num / 10)
    result = House.query.order_by(
        House.publish_time.desc()).paginate(page=page, per_page=10)
    return render_template('list.html', house_list=result.items, page_num=result.page, total_num=total_num)


# 最热房源列表页展示的功能
@list_page.route('/list/hot_house/<int:page>')
def return_hot_list(page):
    # 获取房源总数量
    house_num = House.query.count()
    # 计算总的页码数，向上取整
    total_num = math.ceil(house_num / 10)
    result = House.query.order_by(
        House.publish_time.desc()).paginate(page=page, per_page=10)
    return render_template('list.html', house_list=result.items, page_num=result.page, total_num=total_num)


def deal_title_over(word):
    if len(word) > 15:
        return word[:15] + '...'  # 当房源标题长度大于15时，用省略号替换
    else:
        return word


def deal_direction(word):
    if len(word) == 0 or word is None:  # 房源朝向、交通条件为空时显示暂无信息
        return '暂无信息！'
    else:
        return word


list_page.add_app_template_filter(deal_title_over, 'dealover')
list_page.add_app_template_filter(deal_direction, 'dealdirection')
