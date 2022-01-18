# Microsoft Graph migration

For differences of the underlying API, see [Property differences between Azure AD Graph and Microsoft Graph](https://docs.microsoft.com/graph/migrate-azure-ad-graph-property-differences).

## Breaking changes

Argument breaking changes are listed below. For output JSON breaking changes, please refer to [Property differences between Azure AD Graph and Microsoft Graph](https://docs.microsoft.com/graph/migrate-azure-ad-graph-property-differences).

### `az ad app`

#### `az ad app create`

- `--reply-urls` argument is split into `--web-redirect-uris` and `--public-client-redirect-uris`
- `--homepage` argument is renamed to `--web-home-page-url`
- `--available-to-other-tenants` is replaced by `--sign-in-audience`
- `--native-app` is replaced by `--is-fallback-public-client`
- `--oauth2-allow-implicit-flow` is split into `--implicit-grant-access-token-issuance` and `--implicit-grant-id-token-issuance`

#### `az ad app permission grant`

- `--expires` argument is removed

#### `az ad app credential reset`

- `--credential-description` is replaced by `--display-name`


### `az ad sp`

No breaking change.

### `az ad user`

No breaking change.

### `az ad group`


## Known issues

- Generic update arguments `--add`, `--set` and `--remove` currently don't work. 
- `az ad` and Microsoft Graph related commands fail in Azure Stack environments which don't have Microsoft Graph support

## Command tree

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
