# -*- coding: utf-8 -*-
#/#############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#/#############################################################################

from openerp.osv import fields, orm
from openerp.tools.translate import _


class OeMedicalSignsAndSymptoms(orm.Model):
    _name = 'oemedical.signs_and_symptoms'

    _columns = {
        'clinical_id': fields.many2one('oemedical.pathology',
                                       'Sign or Symptom',required=True ),
        'evaluation_id': fields.many2one('oemedical.patient.evaluation',
                                         string='Evaluation',readonly=True),
        'sign_or_symptom': fields.selection([
            ('sign', 'Sign'),
            ('symptom', 'Symptom'),
        ], string='Subjective / Objective',required=True),
        'comments': fields.char(size=256, string='Comments'),
    }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
