//
// Created by Teo on 3/26/2021.
//

#include "TestServiceAdmin.h"
#include <cassert>

void testServiceAdmin() {
    RepositoryCoats repositoryCoats(10);
    repositoryCoats.initRepository();
    Coat newCoat("M", "IRIS", 135, 10, "https://www.trenchiris.com", "LFKEJSG");
    Coat otherCoat("S", "PEA", 130, 7, "https://www.trenchpea.com", "JDEAXMF");
    ServiceAdministrator serviceAdministrator(repositoryCoats);
    assert(serviceAdministrator.addNewCoatService(newCoat) == false);
    assert(serviceAdministrator.getRepository().getDynamicArray().getLength() == 10);
    newCoat.setUniqueID("qwertyu");
    assert(serviceAdministrator.addNewCoatService(newCoat) == true);
    assert(serviceAdministrator.getRepository().getDynamicArray().getLength() == 11);
    assert(serviceAdministrator.deleteCoatService(otherCoat.getUniqueID()) == false);
    assert(serviceAdministrator.deleteCoatService("somecod") == false);
    otherCoat.setQuantity(0);
    assert(serviceAdministrator.updateCoatService(otherCoat) == true);
    assert(serviceAdministrator.deleteCoatService(otherCoat.getUniqueID()) == true);
    newCoat.setUniqueID("1234567");
    assert(serviceAdministrator.updateCoatService(newCoat) == false);
    assert(serviceAdministrator.getRepository().getDynamicArray().getLength() == 10);
}