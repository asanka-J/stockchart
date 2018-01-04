import MySQLdb
from configparser import ConfigParser
import datetime




def create_db():
    conf = ConfigParser()
    conf.read("../../setup.ini")

    host = conf['mysql']["host"]
#    port = conf['mysql']["port"]
    user = conf['mysql']["username"]
    passwd = conf['mysql']["password"]
    database = conf['mysql']["database"]
    
    mysql = MySQLdb
    db = mysql.connect(host=host,  user=user, passwd=passwd)
    cursor = db.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS {}".format(database)
    cursor.execute(sql)       
    db.close()


def post_datas(datasets):
    conf = ConfigParser()
    conf.read("../../setup.ini")

    host = conf['mysql']["host"]
#    port = conf['mysql']["port"]
    user = conf['mysql']["username"]
    passwd = conf['mysql']["password"]
    database = conf['mysql']["database"]
    
    conn = MySQLdb.connect(host=host,  user=user, passwd=passwd, db=database)
    x = conn.cursor()
    
    
    
    u_id = datasets['id']
    name = datasets['name']
    symbol = datasets['symbol']
    rank = datasets['rank']
    price_usd = datasets['price_usd']
    price_btc = datasets['price_btc']
    volume_usd_24h = datasets['24h_volume_usd']
    market_cap_usd = datasets['market_cap_usd']
    available_supply = datasets['available_supply']
    total_supply = datasets['total_supply']
    max_supply = datasets['max_supply']
    percent_change_1h = datasets['percent_change_1h']
    percent_change_24h = datasets['percent_change_24h']
    percent_change_7d = datasets['percent_change_7d']
    last_updated = str(datetime.datetime.fromtimestamp(int(datasets['last_updated'])))
    images = datasets['graph(7d)']
    history = datasets["history"]


    try:
        x.execute("""INSERT INTO `scrap_post` (`id`, `u_id`, `name`, `symbol`, `rank`, `price_usd`, `price_btc`, `volume_usd_24h`, `market_cap_usd`, `available_supply`, `total_supply`, `max_supply`, `percent_change_1h`, `percent_change_24h`, `percent_change_7d`, `last_updated`, `images`, `history`)
                VALUES (null, '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}', '{15}', {16})"""
              .format(u_id, name, symbol, rank, price_usd, price_btc, volume_usd_24h, market_cap_usd, available_supply, total_supply, max_supply, percent_change_1h, percent_change_24h, percent_change_7d, last_updated, images, history))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)

    conn.close()
    


if __name__ == "__main__":
    
    
    datasets = {'id': 'bitcoin',
                'name': 'Bitcoin',
                'symbol': 'BTC',
                'rank': '1',
                'price_usd': '13274.5',
                'price_btc': '1.0',
                '24h_volume_usd': '10273700000.0',
                'market_cap_usd': '222687370338',
                'available_supply': '16775575.0',
                'total_supply': '16775575.0',
                'max_supply': '21000000.0',
                'percent_change_1h': '-1.54',
                'percent_change_24h': '-1.28',
                'percent_change_7d': '-6.07',
                'last_updated': '1514815459',
                'graph(7d)': 'https://files.coinmarketcap.com/generated/sparklines/1.png',
                'history':1}
    create_db()
#    post_datas(datasets)
        
    


    
