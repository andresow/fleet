/** @odoo-module **/

import { ReportAction } from "@web/webclient/actions/reports/report_action";
import {patch} from "@web/core/utils/patch";
export const ReportActiontype = {
    _onGenerarXMLAccount(event) {
        event.stopPropagation();
		this.props.context['data']=this.props.data
		this.props.context['default_fecha_mes']= this.props.data.month
		this.props.context['default_fecha_ano']= this.props.data.year
		this.props.context['default_procesa_nivel']= this.props.data.show_hierarchy_level
        return this.action.doAction({
            name: "Generar XML",
            type: 'ir.actions.act_window',
            views: [[false, 'form']],
            target: 'new',
            res_model: 'generar.xml.hirarchy.wizard',
			context: this.props.context,
        });

	}
};
patch(
    ReportAction.prototype,
    "contabilidad_cfdi.ClientAction",
    ReportActiontype
);