import time
from flask import Flask, render_template, request
from time import sleep

import parser_bash

#==================#
# Settings - START #
#==================#

hostname = 'RPi-2'

#==================#
# Settings - END #
#==================#

app = Flask(__name__)



@app.route('/system_info')
def system_info():
    v1 = parser_bash.run('cpu_intensive_processes', '../system-information/bash/cpu_intensive_processes.sh')
    v2 = parser_bash.run('ram_intensive_processes', '../system-information/bash/ram_intensive_processes.sh')
    v3 = parser_bash.run('cpu_info', '../system-information/bash/cpu_info.sh')

    # Current ram
    v4 = parser_bash.run('current_ram', '../system-information/bash/current_ram.sh')
    v5 = parser_bash.run('current_ram_total', '../system-information/bash/current_ram.sh')
    v6 = parser_bash.run('current_ram_free', '../system-information/bash/current_ram.sh')
    v7 = parser_bash.run('current_ram_used', '../system-information/bash/current_ram.sh')

    v8 = parser_bash.run('general_info', '../system-information/bash/general_info.sh')
    v9 = parser_bash.run('network_connections', '../system-information/bash/network_connections.sh')
    v10 = parser_bash.run('recent_account_logins', '../system-information/bash/recent_account_logins.sh')

    # Load average
    v11 = parser_bash.run('load_avg_1min', '../system-information/bash/load_avg.sh')
    v12 = parser_bash.run('load_avg_5min', '../system-information/bash/load_avg.sh')

    # Bandwidth
    v13 = parser_bash.run('bandwidth', '../system-information/bash/bandwidth.sh')
    v14 = parser_bash.run('bandwidth_chart', '../system-information/bash/bandwidth.sh')

    v15 = parser_bash.run('arp_cache', '../system-information/bash/arp_cache.sh')

    return render_template('system_info.html',
        hostname=hostname,
        v1=v1,
        v2=v2,
        v3=v3,
        v4=v4,
        v5=v5,
        v6=v6,
        v7=v7,
        v8=v8,
        v9=v9,
        v10=v10,
        v11=v11,
        v12=v12,
        v13=v13,
        v14=v14,
        v15=v15,
    )

    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)

