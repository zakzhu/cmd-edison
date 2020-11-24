# Cmd-Edison

<!-- [![build status][shield-build]][info-build] -->
[![gitter room][shield-gitter]][info-gitter]
[![license][shield-license]][info-license]
[![release][shield-release]][info-release]
[![prs welcome][shield-prs]][info-prs]

> Project description

[TOC]

## Requirements

- **Platforms:**
  - CentOS-7
  - CentOS-8
  - Fedora
  - MacOS
  - Ubuntu
- **Dependencies:**
  - Python >= 3.7
  - PyYAML >= 5.1.2

## Installation

```bash
git clone https://github.com/zakzhu/cmd-edison.git
```

```bash
cd cmd-edison
pip3 install -r requirements.txt
```

## Usage

1. Copy your playbook to directory *playbook/*

   > **NOTE**: The main playbook should be named *site.yml* !   

   ``` bash
   cp Your-Playbook playbook/
   ```

2.  Edit config *flag.yml* 

   ```bash
   vim flag.yml
   ```

## Examples

There is a sample in directory tests/. You could copy the sample files to corresponding directories.

> ```bash
> cp tests/site.yml.sample playbook/
> cp tests/flag.yml.sample flag.yml
> ```

Execute `python main.py --help`, and you would see below:

![](https://gitee.com/zakzhu/md-images/raw/master/cmd-edison/cmd-edison_sample-help.png)

Also you could test more features from this sample.

## Thanks

The following excellent people helped massively:

- [Rowan Manning](https://rowanmanning.com)

## License

Cmd-Edison is licensed under the [BSD-3-Clause][info-license] license.
Copyright &copy; 2020, Zak Zhu

[info-build]: https://travis-ci.org/github/zakzhu/cmd-edison
[info-contribute]: CONTRIBUTING.md
[info-faq]: FAQ.md
[info-gitter]: https://gitter.im/zakzhu/cmd-edison
[info-license]: LICENSE
[info-release]: https://github.com/zakzhu/cmd-edison/releases
[info-prs]: https://github.com/zakzhu/cmd-edison/pulls
[shield-build]: https://img.shields.io/travis/zakzhu/cmd-edison
[shield-gitter]: https://img.shields.io/gitter/room/zakzhu/cmd-edison
[shield-license]: https://img.shields.io/github/license/zakzhu/cmd-edison
[shield-release]: https://img.shields.io/github/v/release/zakzhu/cmd-edison
[shield-prs]: https://img.shields.io/badge/PRs-welcome-brightgreen
