Name:       resalloc-aws
Summary:    Resource allocator scripts for AWS
Version:    1.3
Release:    3%{?dist}
License:    GPLv2+
URL:        https://github.com/praiskup/resalloc-aws
BuildArch:  noarch

Requires: awscli

# Source is created by:
# git clone %%url && cd copr
# tito build --tgz --tag %%name-%%version-%%release
Source0: %{name}-%{version}.tar.gz

# This one is bundled, though it is GPLv2+, too.
Source1: https://raw.githubusercontent.com/praiskup/wait-for-ssh/main/wait-for-ssh


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
sed '1c#! %{__python3}' %SOURCE1 > %{name}-wait-for-ssh


%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 bin/resalloc-aws-new %{buildroot}%{_bindir}
install -p -m 0755 bin/resalloc-aws-delete %{buildroot}%{_bindir}
install -p -m 0755 bin/resalloc-aws-list %{buildroot}%{_bindir}
install -p -m 0755 %{name}-wait-for-ssh %{buildroot}%{_bindir}/resalloc-aws-wait-for-ssh


%files
%license COPYING
%doc README.md
%{_bindir}/%{name}-delete
%{_bindir}/%{name}-new
%{_bindir}/%{name}-list
%{_bindir}/%{name}-wait-for-ssh


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Pavel Raiskup <praiskup@redhat.com> 1.3-1
- New script resalloc-aws-list

* Tue Mar 22 2022 Pavel Raiskup <praiskup@redhat.com> 1.2-1
- resalloc-aws-new: tag volumes started with new instances

* Fri Oct 15 2021 Pavel Raiskup <praiskup@redhat.com> 1.1-1
- spec: package-review fixes (praiskup@redhat.com)

* Tue Oct 12 2021 Pavel Raiskup <praiskup@redhat.com> 1-1
- new package built with tito
