# property tax calculator 1
def main():
    print('\n'*5.5)
    nheac = .004
    mwrdc = .406
    pmab = .006
    cpd = .362
    MiscTx = nheac + mwrdc + pmab + cpd
    bec = 3.726
    cccd = .169
    Schooltax = bec + cccd
    csbif=.128
    clf=.122
    city = 1.630
    City = csbif + clf + city    
    ccfpd = .063
    cook = .316
    ccps = .130
    cchf = .087
    CookCty = cfpd + cook + ccps + cchf
    TotalTaxRate = MiscTax + SchoolTax + City + CookCty
    print('Property Tax Rate is: ', TotalTaxRate)
main()
