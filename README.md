# Monkey Nodes

A repo with nodes for monkeying around on ComfyUI

![Chief Monkey Officer (Rémi)](/images/remi.png)


## Nodes

### Image Size Align

Pad the image, so the image dimensions are a multiple of the **modulus**
parameter. Padding pixels are added on top and left sides of the image.

## Developer notes

### Versioning / Releasing

We use conventional commits and semver, managed by the
[Commitizen](https://commitizen-tools.github.io/commitizen/) tool to handle
versionning and tagging.

To create a new release use:

``` shellsession
cz bump
git push origin --tags
```
