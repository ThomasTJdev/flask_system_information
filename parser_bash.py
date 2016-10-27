import subprocess 
import shlex 
import json
from time import sleep


# ========================================================= #
#=                    Run command once                     =#
# ========================================================= #
def run_commandOnce(command):
    try:
        # Use command arg
        # Use shlex for easy command formatting
        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            return ("Fail")
        if output:
            return output.strip()
        #rc = process.poll()
        #return rc

    except:
        # Missing fail procedures
        return "Fail"


# =========================================================== #
#= Continuous running, not used. To be used for live charts. =#
# =========================================================== #
def run_commandConstant(command):
    while True:
        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            return ("Fail")
        if output:
            return output.strip()
        sleep(2)
    #rc = process.poll()
    #return rc


# ========================================================= #
#=             Parse and print json, not used              =#
# ========================================================= #
def parseJson(dataJson):
    """ Open json file """
    data = json.loads(dataJson)

    out = '"time"'
    for dest in data:
       out = out + ', ' + str(dest["pid"])

    return out


# ========================================================= #
#=         1) Parse data 2) Output in HTML                 =#
# ========================================================= #
def parseJsonHTMLtable(typeInfo, dataJson):
    # Open json file
    data = json.loads(dataJson)

    out2 = ''

    # cpu_intensive_processes
    if typeInfo == "cpu_intensive_processes":
        out1 = (
            '<table class="table table-inverse system_information">' +
            '<thead>' + '<tr>' +
            '<th>' + "pid" + '</th>' +
            '<th>' + "user" + '</th>' +
            '<th>' + "cpu%" + '</th>' +
            '<th>' + "rss" + '</th>' +
            '<th>' + "vsz" + '</th>' +
            '<th>' + "cmd" + '</th>' +
            '</tr>' + '</thead>' + '<tbody>')

        for dest in data:
           out2 = (
                out2 +
                '<tr>' +
                '<td>' + str(dest["pid"]) + '</td>' +
                '<td>' + str(dest["user"]) + '</td>' +
                '<td>' + str(dest["cpu%"]) + '</td>' +
                '<td>' + str(dest["rss"]) + '</td>' +
                '<td>' + str(dest["vsz"]) + '</td>' +
                '<td>' + str(dest["cmd"]) + '</td>' +
                '</tr>')
        out = out1 + out2 + '</tbody></table>'


    # ram_intensive_processes
    if typeInfo == "ram_intensive_processes":
        out1 = (
            '<table class="table table-inverse system_information">' +
            '<thead>' + '<tr>' +
            '<th>' + "pid" + '</th>' +
            '<th>' + "user" + '</th>' +
            '<th>' + "mem%" + '</th>' +
            '<th>' + "rss" + '</th>' +
            '<th>' + "vsz" + '</th>' +
            '<th>' + "cmd" + '</th>' +
            '</tr>' + '</thead>' + '<tbody>')

        for dest in data:
           out2 = (
                out2 +
                '<tr>' +
                '<td>' + str(dest["pid"]) + '</td>' +
                '<td>' + str(dest["user"]) + '</td>' +
                '<td>' + str(dest["mem%"]) + '</td>' +
                '<td>' + str(dest["rss"]) + '</td>' +
                '<td>' + str(dest["vsz"]) + '</td>' +
                '<td>' + str(dest["cmd"]) + '</td>' +
                '</tr>')
        out = out1 + out2 + '</tbody></table>'


    # cpu_info
    elif typeInfo == "cpu_info":
        out1 = '<table class="table table-inverse system_information">'

        for dest in data:
           out2 = (
                out2 +
                '<tr>' +
                '<td>' + "Architecture" + '</td>' +
                '<td>' + dest["Architecture"] + '</td>' +
                '</tr><tr>' +
                '<td>' + "Byte Order" + '</td>' +
                '<td>' + dest["Byte Order"] + '</td>' +
                '</tr><tr>' +
                '<td>' + "CPU(s)" + '</td>' +
                '<td>' + dest["CPU(s)"] + '</td>' +
                '</tr><tr>' +
                '<td>' + "Online CPU(s) list" + '</td>' +
                '<td>' + dest["On-line CPU(s) list"] + '</td>' +
                '</tr><tr>' +
                '<td>' + "Thread(s)/cores" + '</td>' +
                '<td>' + dest["Thread(s) per core"] + '</td>' +
                '</tr><tr>' +
                '<td>' + "Core(s)/socket" + '</td>' +
                '<td>' + dest["Core(s) per socket"] + '</td>' +
                '</tr><tr>' +
                '<td>' + "Socket(s)" + '</td>' +
                '<td>' + dest["Socket(s)"] + '</td>' +
                '</tr><tr>' +
                '<td>' + "Model name" + '</td>' +
                '<td>' + dest["Model name"] + '</td>' +
                '</tr><tr>' +
                '<td>' + "CPU max MHz" + '</td>' +
                '<td>' + dest["CPU max MHz"] + '</td>' +
                '</tr><tr>' +
                '<td>' + "CPU min MHz" + '</td>' +
                '<td>' + dest["CPU min MHz"] + '</td>' +
                '</tr>')
        out = out1 + out2 + '</tbody></table>'


    # current ram
    elif typeInfo == "current_ram":
        for dest in data:
           out2 = (
                out2 +
                '["total", ' + str(dest["total"]) + '],' +
                '["used", ' + str(dest["used"]) + '],' +
                '["free", ' + str(dest["free"]) + ']' +
                '')
        out = out2

    elif typeInfo == "current_ram_total":
        for dest in data:
            out = str(dest["total"])

    elif typeInfo == "current_ram_free":
        for dest in data:
            out = str(dest["free"])

    elif typeInfo == "current_ram_used":
        for dest in data:
            out = str(dest["used"])



    # general_info
    elif typeInfo == "general_info":
        out1 = '<table class="table table-inverse system_information">'
        for dest in data:
           out2 = (
                out2 +
                '<tr>' +
                '<td>' + 'OS: ' + '</td>' +
                '<td>' + dest["OS"] + '</td>' +
                '</tr><tr>' +
                '<td>' + 'Hostname: ' + '</td>' +
                '<td>' + dest["Hostname"] + '</td>' +
                '</tr><tr>' +
                '<td>' + 'Uptime: ' + '</td>' +
                '<td>' + dest["Uptime"] + '</td>' +
                '</tr><tr>' +
                '<td>' + 'Server Time: ' + '</td>' +
                '<td>' + dest["Server Time"] + '</td>' +
                '</tr>')
        out = out1 + out2 + '</table>'



    elif typeInfo == "network_connections":
        out1 = (
            '<table class="table table-inverse system_information">' +
            '<thead>' + '<tr>' +
            '<th>' + "Connections" + '</th>' +
            '<th>' + "Address" + '</th>' +
            '</tr>' + '</thead>' + '<tbody>')

        for dest in data:
           out2 = (
                out2 +
                '<tr>' +
                '<td>' + str(dest["connections"]) + '</td>' +
                '<td>' + dest["address"] + '</td>' +
                '</tr>')
        out = out1 + out2 + '</tbody></table>'



    # recent_account_logins
    elif typeInfo == "recent_account_logins":
        out1 = (
            '<table class="table table-inverse system_information">' +
            '<thead>' + '<tr>' +
            '<th>' + "User" + '</th>' +
            '<th>' + "IP" + '</th>' +
            '<th>' + "Date" + '</th>' +
            '</tr>' + '</thead>' + '<tbody>')

        for dest in data:
           out2 = (
                out2 +
                '<tr>' +
                '<td>' + dest["user"] + '</td>' +
                '<td>' + dest["ip"] + '</td>' +
                '<td>' + dest["date"] + '</td>' +
                '</tr>')
        out = out1 + out2 + '</tbody></table>'



    elif typeInfo == "load_avg_1min":
        for dest in data:
            return str(dest["1_min_avg"])

    elif typeInfo == "load_avg_5min":
        for dest in data:
            return str(dest["5_min_avg"])

    elif typeInfo == "load_avg_15min":
        for dest in data:
            return str(dest["15_min_avg"])


    # bandwidth
    # missing lots of info: drops, accept, etc
    elif typeInfo == "bandwidth":
        out1 = (
            '<table class="table table-inverse system_information">' +
            '<thead>' + '<tr>' +
            '<th>' + "Interface" + '</th>' +
            '<th>' + "Tx" + '</th>' +
            '<th>' + "Rx" + '</th>' +
            '</tr>' + '</thead>' + '<tbody>')

        for dest in data:
           out2 = (
                out2 +
                '<tr>' +
                '<td>' + dest["interface"] + '</td>' +
                '<td>' + str(dest["tx"]) + '</td>' +
                '<td>' + str(dest["rx"]) + '</td>' +
                '</tr>')
        out = out1 + out2 + '</tbody></table>'

    # bandwidth_chart
    elif typeInfo == "bandwidth_chart":
        for dest in data:
           out2 = (
                out2 +
                '["' +
                dest["interface"] + '", ' +
                str(dest["tx"]) + ', ' +
                str(dest["rx"]) +
                '],')
        out2 = str(out2)[0:-1]
        out = out2


    # arp_cache
    elif typeInfo == "arp_cache":
        out1 = (
            '<table class="table table-inverse system_information">' +
            '<thead>' + '<tr>' +
            '<th>' + "Address" + '</th>' +
            '<th>' + "HW_type" + '</th>' +
            '<th>' + "HW_address" + '</th>' +
            '<th>' + "Flags" + '</th>' +
            '<th>' + "Mask" + '</th>' +
            '</tr>' + '</thead>' + '<tbody>')

        for dest in data:
           out2 = (
                out2 +
                '<tr>' +
                '<td>' + dest["address"] + '</td>' +
                '<td>' + dest["hw_type"] + '</td>' +
                '<td>' + dest["hw_address"] + '</td>' +
                '<td>' + dest["flags"] + '</td>' +
                '<td>' + dest["mask"] + '</td>' +
                '</tr>')
        out = out1 + out2 + '</table>'


    else:
        out2 = (
            '<tr>' +
            '<td>Error, wrong type of info defined in function</td>' +
            '</tr>')



    return out



# ========================================================= #
#= The combiner. 1) Run sh, 2) Parse data, 3) Return/print =#
# ========================================================= #
def run(typeInfo, command):
    data = run_commandOnce(command)
    data = str(data)[2:-1]
    out = parseJsonHTMLtable(typeInfo, data)
    # You just wanne print it? Remove # from print.
    #print (out)
    return out


# ========================================================= #
#=                      Run all sh                         =#
# ========================================================= #
def main():
    # This function includes all the system information bash scripts

    run('cpu_intensive_processes', './bash/cpu_intensive_processes.sh')
    run('ram_intensive_processes', './bash/ram_intensive_processes.sh')
    run('cpu_info', './bash/cpu_info.sh')

    # Current ram
    run('current_ram', './bash/current_ram.sh')
    run('current_ram_total', './bash/current_ram.sh')
    run('current_ram_free', './bash/current_ram.sh')
    run('current_ram_used', './bash/current_ram.sh')

    run('general_info', './bash/general_info.sh')
    run('network_connections', './bash/network_connections.sh')
    run('recent_account_logins', './bash/recent_account_logins.sh')

    # Load average
    run('load_avg_1min', './bash/load_avg.sh')
    run('load_avg_5min', './bash/load_avg.sh')

    # Bandwidth
    run('bandwidth', './bash/bandwidth.sh')
    run('bandwidth_chart', './bash/bandwidth.sh')

    run('arp_cache', './bash/arp_cache.sh')


#main()
