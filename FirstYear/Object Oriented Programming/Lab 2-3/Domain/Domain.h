//
// Created by Teo on 3/11/2021.
//

#ifndef A23_ALEXTEO24_DOMAIN_H
#define A23_ALEXTEO24_DOMAIN_H

typedef struct {
    char* estateType;
    char* estateAddress;
    int estateSurface;
    int estatePrice;
}Estate;

Estate * createEstate(char* estateType, char* estateAddress, int estateSurface, int estatePrice);

void destroyEstate(Estate * someEstate);

Estate * copyEstate(Estate * someEstate);

#endif //A23_ALEXTEO24_DOMAIN_H
