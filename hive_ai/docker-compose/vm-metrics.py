from flask import Flask, jsonify
import psutil


app = Flask(__name__)


# Helper function to convert bytes to megabytes
def bytes_to_mb(size_bytes):
    return round(size_bytes / (1024 * 1024), 2)


# Route for CPU metrics
@app.route('/metrics/cpu')
def cpu_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()


    cpu_info = {
        'percent': f"{cpu_percent}%",
        'count': cpu_count
    }
    return jsonify(cpu_info)


# Route for memory metrics
@app.route('/metrics/memory')
def memory_metrics():
    memory_info = psutil.virtual_memory()
    memory_total = bytes_to_mb(memory_info.total)
    memory_used = bytes_to_mb(memory_info.used)
    memory_free = bytes_to_mb(memory_info.free)


    memory_data = {
        'total_MB': memory_total,
        'used_MB': memory_used,
        'free_MB': memory_free
    }
    return jsonify(memory_data)


# Route for disk metrics
@app.route('/metrics/disk')
def disk_metrics():
    disk_usage = psutil.disk_usage('/')
    disk_total = bytes_to_mb(disk_usage.total)
    disk_used = bytes_to_mb(disk_usage.used)
    disk_free = bytes_to_mb(disk_usage.free)


    disk_data = {
        'total_MB': disk_total,
        'used_MB': disk_used,
        'free_MB': disk_free
    }
    return jsonify(disk_data)


# Route for network metrics (system-wide and per interface)
@app.route('/metrics/network')
def network_metrics():
    # System-wide network metrics
    network_info = psutil.net_io_counters()
    system_wide = {
        'bytes_sent_MB': bytes_to_mb(network_info.bytes_sent),
        'bytes_recv_MB': bytes_to_mb(network_info.bytes_recv),
        'packets_sent': network_info.packets_sent,
        'packets_recv': network_info.packets_recv
    }


    # Per-interface network metrics
    net_per_interface = psutil.net_io_counters(pernic=True)
    interface_stats = {}
    for interface, stats in net_per_interface.items():
        interface_stats[interface] = {
            'bytes_sent_MB': bytes_to_mb(stats.bytes_sent),
            'bytes_recv_MB': bytes_to_mb(stats.bytes_recv),
            'packets_sent': stats.packets_sent,
            'packets_recv': stats.packets_recv
        }


    network_data = {
        'system_wide_MB': system_wide,
        'per_interface_MB': interface_stats
    }
    return jsonify(network_data)


# Route to return all system metrics in one response
@app.route('/metrics')
def all_metrics():
    # Get CPU metrics
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()


    # Get memory metrics
    memory_info = psutil.virtual_memory()
    memory_total = bytes_to_mb(memory_info.total)
    memory_used = bytes_to_mb(memory_info.used)
    memory_free = bytes_to_mb(memory_info.free)


    # Get disk usage
    disk_usage = psutil.disk_usage('/')
    disk_total = bytes_to_mb(disk_usage.total)
    disk_used = bytes_to_mb(disk_usage.used)
    disk_free = bytes_to_mb(disk_usage.free)


    # Get network metrics (system-wide and per interface)
    network_info = psutil.net_io_counters()
    system_wide = {
        'bytes_sent_MB': bytes_to_mb(network_info.bytes_sent),
        'bytes_recv_MB': bytes_to_mb(network_info.bytes_recv),
        'packets_sent': network_info.packets_sent,
        'packets_recv': network_info.packets_recv
    }


    net_per_interface = psutil.net_io_counters(pernic=True)
    interface_stats = {}
    for interface, stats in net_per_interface.items():
        interface_stats[interface] = {
            'bytes_sent_MB': bytes_to_mb(stats.bytes_sent),
            'bytes_recv_MB': bytes_to_mb(stats.bytes_recv),
            'packets_sent': stats.packets_sent,
            'packets_recv': stats.packets_recv
        }


    # Prepare response
    metrics = {
        'cpu': {
            'percent': f"{cpu_percent}%",
            'count': cpu_count
        },
        'memory': {
            'total_MB': memory_total,
            'used_MB': memory_used,
            'free_MB': memory_free
        },
        'disk': {
            'total_MB': disk_total,
            'used_MB': disk_used,
            'free_MB': disk_free
        },
        'network': {
            'system_wide_MB': system_wide,
            'per_interface_MB': interface_stats
        }
    }


    return jsonify(metrics)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
