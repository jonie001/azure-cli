# Microsoft Graph migration

## Breaking changes

### `az ad app`

`az ad app permission grant`: `--expires` argument is removed

### `az ad sp`

### `az ad user`

### `az ad group`



```
az ad
  app
    credential
      delete
      list
      reset
    owner
      add
      list
      remove
    permission
      add
      admin-consent
      delete
      grant
      list
      list-grants
    create
    delete
    list
    show
    update
  group
    member
      add
      check
      list
      remove
    owner
      add
      list
      remove
    create
    delete
    get-member-groups
    list
    show
  signed-in-user
    list-owned-objects
    show
  sp
    credential
      delete
      list
      reset
    owner
      list
    create
    create-for-rbac
    delete
    list
    show
    update
  user
    create
    delete
    get-member-groups
    list
    show
    update
```
