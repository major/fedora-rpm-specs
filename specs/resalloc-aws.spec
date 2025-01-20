Name:       resalloc-aws
Summary:    Resource allocator scripts for AWS
Version:    1.8
Release:    4%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
URL:        https://github.com/praiskup/resalloc-aws
BuildArch:  noarch

Requires:   awscli
Requires:   resalloc-helpers

# Source is created by:
# git clone %%url && cd copr
# tito build --tgz --tag %%name-%%version-%%release
Source0: %{name}-%{version}.tar.gz


%description
When allocating/removing a machine in AWS/EC2 from command-line, there are many
non-trivial options in the 'aws-cli' command.  This project provides a
simplified wrapping command.

The 'resalloc-aws-new' script is able to (a) start a machine, (b) wait till SSH
is available and (c) run a specified playbook.

The 'resalloc-aws-delete' removes a machine started by 'resalloc-aws-new'
script.

These scripts are primarily designed to be used with 'resalloc-server', but they
might be used separately.


%prep
%setup -q


%build


%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 bin/resalloc-aws-new %{buildroot}%{_bindir}
install -p -m 0755 bin/resalloc-aws-delete %{buildroot}%{_bindir}
install -p -m 0755 bin/resalloc-aws-list %{buildroot}%{_bindir}
install -p -m 0755 bin/resalloc-aws-minimal-spot-zone %{buildroot}%{_bindir}


%files
%license COPYING
%doc README.md
%{_bindir}/%{name}-delete
%{_bindir}/%{name}-new
%{_bindir}/%{name}-list
%{_bindir}/%{name}-minimal-spot-zone


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 28 2024 Pavel Raiskup <praiskup@redhat.com> 1.8-1
- The wait-for-ssh script moved to resalloc-helpers

* Thu Nov 23 2023 Pavel Raiskup <praiskup@redhat.com> 1.7-1
- resalloc-aws-new: run playbook with stdin=/dev/null
- resalloc-aws-list: no need to double-kill "shutting-down" instances

* Wed Nov 22 2023 Pavel Raiskup <praiskup@redhat.com> 1.6-1
- resalloc-aws-list: don't list terminated instances
- resalloc-aws-minimal-spot-zone helper

* Fri Sep 01 2023 Pavel Raiskup <praiskup@redhat.com> 1.5-1
- resalloc-aws-new: add `--root-volume-size` option (svashisht@redhat.com)

* Wed May 10 2023 Pavel Raiskup <praiskup@redhat.com> 1.4-1
- resalloc-aws-new: use gp3 volume for the root filesystem (frostyx@email.cz)
- Update the wait-for-ssh submodule (praiskup@redhat.com)

* Wed Jun 22 2022 Pavel Raiskup <praiskup@redhat.com> 1.3-1
- New script resalloc-aws-list

* Tue Mar 22 2022 Pavel Raiskup <praiskup@redhat.com> 1.2-1
- resalloc-aws-new: tag volumes started with new instances

* Fri Oct 15 2021 Pavel Raiskup <praiskup@redhat.com> 1.1-1
- spec: package-review fixes (praiskup@redhat.com)

* Tue Oct 12 2021 Pavel Raiskup <praiskup@redhat.com> 1-1
- new package built with tito
