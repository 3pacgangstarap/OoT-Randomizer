#include "z64.h"
#include "get_items.h"
#include "scene.h"
#include "actor.h"
#include "models.h"
#include "fishing.h"


extern xflag_t* spawn_actor_with_flag;

z64_actor_t* Fishing_Actor_Spawn_Hook(void* actorCtx, z64_game_t* globalCtx, int16_t actorId, float posX, float posY, float posZ, int16_t rotX, int16_t rotY, int16_t rotZ, int16_t params) {
    xflag_t fish_flag = { 0 };
    fish_flag.room = globalCtx->room_index;
    fish_flag.scene = globalCtx->scene_index;
    fish_flag.setup = curr_scene_setup;
    fish_flag.flag = globalCtx->link_age; // Use the current age as the flag to distinguish child/adult fish
    fish_flag.subflag = params - 100; // Params contains the value 100 + i from the spawn loop. Add 1
    spawn_actor_with_flag = &fish_flag;
    Fishing* fish = z64_SpawnActor(actorCtx, globalCtx, actorId, posX, posY, posZ, rotX, rotY, rotZ, params);
    fish->override = get_newflag_override(&fish->actor, globalCtx);
    spawn_actor_with_flag = NULL;
    return fish;
}

extern void Fishing_DrawFish(z64_actor_t* this, z64_game_t* globalCtx);
void Fishing_SkeletonDraw_Hook(z64_game_t* globalCtx, void** skeleton, z64_xyz_t* jointTable, int32_t dListCount, OverrideLimbDrawOpa overrideLimbDraw, PostLimbDrawOpa postLimbDraw, void* this) {
    Fishing* fish = (Fishing*)this;
    if(fish->override.key.all) {
        postLimbDraw(globalCtx, fish->isLoach ? 0x0B : 0x0D, NULL, NULL, this); // Call the postLimbDraw function. This is used to set the mouth position which affects where the lure moves.
        fishing_draw(&(fish->actor), globalCtx);
        return;
    }
    SkelAnime_DrawFlexOpa(globalCtx, skeleton, jointTable, dListCount, overrideLimbDraw, postLimbDraw, this);
    //Fishing_DrawFish(this, globalCtx);
}