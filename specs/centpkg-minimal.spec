Name:           centpkg-minimal
Version:        2.1.0
Release:        6%{?dist}
Summary:        Used by koji to download sources for building CentOS

License:        GPL-2.0-only
URL:            https://git.centos.org/centos-git-common
Source0:        %{name}.tar.gz
Source1:        centpkg

BuildArch:      noarch
Requires:       util-linux
Requires:       curl
Requires:       git-core
Conflicts:      centpkg

%description
Used by koji to download sources for building CentOS

%prep
%setup -c -n centpkg-minimal
cp %{SOURCE1} .

%build


%install
install -d %{buildroot}%{_bindir}
install -pm 755 get_sources.sh %{buildroot}%{_bindir}/get_sources.sh
install -pm 755 centpkg %{buildroot}%{_bindir}/centpkg


%files
%{_bindir}/get_sources.sh
%{_bindir}/centpkg


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 06 2024 Troy Dawson <tdawson@redhat.com> - 2.1.0-5
- Use correct SPDX License
- Use sources.stream.centos.org for downloading sources

* Mon Apr 04 2022 bstinson@redhat.com - 2.1.0-4
- Bump for a new tarball

* Wed Mar 30 2022 bstinson@redhat.com - 2.1.0-3
- Update to include a new get_sources.sh

* Fri Mar 05 2021 bstinson@redhat.com - 2.1.0-2
- Add a minimal centpkg binary that calls get_sources or pulls from the CentOS
  Stream lookaside based on which layout the repo presents

* Tue Jun 18 2019 brian@bstinson.com - 2.0.0-2
- Update the git dep to git-core to pull in fewer deps

* Tue May 07 2019 Brian Stinson <brian@bstinson.com> - 2.0.0-1
- Release for GA

* Tue Apr 30 2019 Brian Stinson <brian@bstinson.com> - 1.0.0-9
- rebuilt

* Mon Apr 15 2019 Brian Stinson <brian@bstinson.com> - 1.0.0-8
- rebuilt

* Mon Apr 15 2019 Brian Stinson <brian@bstinson.com> - 1.0.0-7
- rebuilt

* Mon Apr 15 2019 Brian Stinson <brian@bstinson.com> - 1.0.0-6
- rebuilt

* Mon Apr 15 2019 brian@bstinson.com - 1.0.0-4
- Update to not require 'which'

* Mon Apr 15 2019 Brian Stinson <brian@bstinson.com> - 1.0.0-4
- rebuilt

* Mon Apr 15 2019 Brian Stinson <brian@bstinson.com> - 1.0.0-3
- Added requires

* Mon Apr 15 2019 Brian Stinson <brian@bstinson.com> - 1.0.0-2
- rebuilt

* Mon Apr 15 2019 brian@bstinson.com - 1.0.0-1
- Initial release
