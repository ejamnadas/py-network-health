import dtma_ntw_health_tasks as tasks
import variables as var

#def lambda_handler(event, context):
tasks.last_hb_in_min_fail('LQS')
tasks.last_hb_in_min_fail('LQR')
#tasks.last_hb_in_min_fail(var.getProperty())
#tasks.last_hb_in_min_fail(var.getProperty())