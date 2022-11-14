import view
import guid
import logger


def button_click():
    value_a = view.get_value()
    oper = view.get_operator()
    value_b = view.get_value()
    func = guid.dict_ar[oper]
    func.init(value_a, value_b)
    result = func.do_it()
    view.get_result(result)
    operation = guid.dict_log[oper]
    logger.get_log(result, operation)