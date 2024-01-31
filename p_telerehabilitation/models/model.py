from odoo import api, fields, models

class pt_session(models.Model):

    _name = 'pt_session'
    _description = 'session'
    name = fields.Char("session")
    patient_id = fields.Many2one(comodel_name='pt_patient',string='Patient_id',required=False)
    doctor_id = fields.Many2one(comodel_name='pt_doctor', string='doctor_id', required=False)
    jitsi_meet_id = fields.Many2one(comodel_name='sinerkia_jitsi_meet.jitsi_meet', string='jitsi_meet', required=False)
    lin_training_ids = fields.One2many(comodel_name='pt_lin_training',inverse_name='session_id',string='Training_ids',required=False)
    note = fields.Html(string="note")
    url = fields.Char("url")
    url2 = fields.Char("url2" )
    url1 = fields.Char(string='URL to Meeting', related='jitsi_meet_id.url')

    @api.multi
    def open1(self):
        self.get_url()
        return {'name': 'JITSI MEET',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': self.url1
                }

    @api.multi
    def open(self):
        self.get_url()
        return {'name': 'JITSI MEET',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': self.url
                }
    @api.multi
    def open2(self):
        return {'name': 'JITSI MEET',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': self.url2
                }
    @api.onchange('patient_id')
    def get_url(self):
        try:
            
            base_url = self.env['ir.config_parameter'].get_param('web.base.url')
            url=base_url+"/aa"
            url2=base_url+"/aa2"
            # r=self.patient_id.id
            # if r:
            #     s=self._origin.id
            #     url=base_url+"/aa?r="+str(r)+"&s="+str(s)
            #     url2=base_url+"/aa2?r="+str(r)+"&s="+str(s)
            #     url.replace(" ", "")
            #     url2.replace(" ", "")
            # else:
            #     url=""
            #     url2=""

            self.url=url
            self.url2=url2
        except Exception as e:
            pass
            # raise e
        
class pt_patient(models.Model):
    _name = 'pt_patient'
    _inherits = {'res.users': "users_id"}
    _description = 'patient'
    name2 = fields.Char("patient")
    date_of_Birth = fields.Date( string='Date of Birth', required=False)
    Title = fields.Char("Title")
    blood_group = fields.Char("blood_group")
    job2 = fields.Char("job")
    National_ID = fields.Char("National ID")
    note = fields.Html(string="note")
    gender = fields.Selection(string='gender', selection=[('male', 'male'), ('female', 'Female')], )

    @api.onchange('name')
    def onchange_method(self):
        group_id = self.env.ref('p_telerehabilitation.pt_mal')
        self.groups_id = group_id


class pt_doctor (models.Model):
    _name = 'pt_doctor'
    _description = 'doctor'
    _inherits = {'res.users': "users_id"}
    name2 = fields.Char("doctor")
    date_of_Birth= fields.Date(
        string='Date of Birth',
        required=False)
    blood_group = fields.Char("blood_group")
    Title=fields.Char("Title")
    job=fields.Char("job")
    National_ID=fields.Char("National ID")

    note = fields.Html(string="note")


    gender = fields.Selection(string='gender',selection=[('male', 'male'), ('female', 'Female')],)

    @api.onchange('name')
    def onchange_method(self):
        group_id = self.env.ref('p_telerehabilitation.pt_dr')
        self.groups_id = group_id


class pt_training (models.Model):
    _name = 'pt_training'
    _description = 'training'
    name = fields.Char("training")
    doctor_id = fields.Many2one(comodel_name='pt_doctor', string='doctor_id', required=False)
    description = fields.Html(string="Description")
class pt_lin_training (models.Model):
    _name = 'pt_lin_training'
    _description = 'lin_training'

    name = fields.Char("lin_training")
    session_id = fields.Many2one(comodel_name='pt_session', string='session_id', required=False)
    training_id = fields.Many2one(comodel_name='pt_training', string='training_id', required=False)

    description = fields.Html(string="Description",related='training_id.description')
    name_t = fields.Char("name",related='training_id.name')
    note = fields.Html(string="note")





# class pt_training (models.Model):
#     _name = 'pt_training'
#     _description = 'training'
#     name = fields.Char("training")
