{
    "name": "p_telerehabilitation",
    "version": '0.0.0',
    "license": "LGPL-3",
    "author": "g_glass",
    "website": "https://www.p_telerehabilitation.at",
    "depends": [
        "base",
        "sinerkia_jitsi_meet",
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/views_doctor.xml",
        "views/views_patient.xml",
        "views/views_session.xml",
        "views/views_training.xml",
        "views/views_template.xml",
        "views/views_template2.xml",
        # "views/views.xml",



    ],
    "images": [
        # 'static/img/logo.png',
        #
    ],
    "sequence": 3,
    "application": True,
    "installable": True,
    "auto_install": True,
}
