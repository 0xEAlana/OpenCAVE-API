class AWIPScli:
    def __init__(self, awipsserver= 'edex-cloud.unidata.ucar.edu'):
        
        awipsservers = [
            'edex-cloud.unidata.ucar.edu',
            'thredds.ucar.edu',
            'unidata.ucar.edu',
        ]
        self.altserver = awipsservers