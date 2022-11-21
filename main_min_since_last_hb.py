import dtma_ntw_health_tasks as tasks
import variables as var

#def lambda_handler(event, context):
tasks.last_hb_in_min_fail(var.getProperty())