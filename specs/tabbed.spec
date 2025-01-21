# XXX: Drop once f36 goes EOL
%if 0%{?fedora} == 036
%undefine _package_note_file
%endif

Name:           tabbed
Version:        0.7
Release:        6%{?dist}
Summary:        Simple Xembed container manager

%global         _tabbedsourcedir %{_usrsrc}/tabbed-user-%{version}-%{release}

License:        MIT
URL:            http://tools.suckless.org/tabbed
Source0:        http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
Source1:        %{name}-user
Source2:        %{name}-user.1
# Upstream tarball doesn't include the xembed manpage in 0.6; taken from
# the git repository (fixed in 910e67db).
Source3:        xembed.1
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  fontconfig-devel
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  make
BuildRequires:  sed
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives


%description
A simple generic fronted to XEmbed aware applications.

%package user
Summary:        Tabbed sources and tools for user configuration
License:        MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       binutils
Requires:       coreutils
Requires:       findutils
Requires:       fontconfig-devel
Requires:       gcc
Requires:       libX11-devel
Requires:       libXft-devel
Requires:       make
Requires:       patch
Requires:       redhat-rpm-config
Requires:       sed
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description user
Tabbed source files and a launcher/builder wrapper script for
customized configurations.

%prep
%setup -q
# XXX: To be dropped with 0.8+
cp %{SOURCE3} .
sed -e 's|/usr/local|%{_prefix}|g' \
    -e 's|/usr/lib|%{_libdir}|g' \
    -e 's|-std=c99 -pedantic -Wall -Os|%{optflags}|g' \
    -e 's|-s\b||' \
    -e 's|\(${LIBS}\)|\1 %{?__global_ldflags}|' \
    -i config.mk
sed -i 's!^\(\t\+\)@!\1!' Makefile 

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_bindir}/%{name}{,-fedora}
install -pm755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}-user
install -Dpm644 %{SOURCE2} %{buildroot}%{_mandir}/man1/%{name}-user.1
for file in \
    %{buildroot}%{_bindir}/%{name}-user \
    %{buildroot}%{_mandir}/man1/%{name}-user.1; do
sed -i -e 's/VERSION/%{version}/' \
       -e 's/RELEASE/%{release}/' \
       ${file}
done
mkdir -p %{buildroot}%{_tabbedsourcedir}
install -m644 arg.h config.def.h config.mk Makefile tabbed.c xembed.c \
     %{buildroot}%{_tabbedsourcedir}
touch %{buildroot}%{_bindir}/%{name}

%pre
[ -L %{_bindir}/%{name} ] || rm -f %{_bindir}/%{name}

%post
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} %{name} \
    %{_bindir}/%{name}-fedora 10

%postun
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}-fedora
fi

%post user
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} %{name} \
    %{_bindir}/%{name}-user 20

%postun user
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}-user
fi

%files
%doc LICENSE README
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}-fedora
%{_bindir}/xembed
%{_mandir}/man1/%{name}.*
%{_mandir}/man1/xembed.*

%files user
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}-user
%{_mandir}/man1/%{name}-user.*
%{_tabbedsourcedir}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Petr Šabata <contyk@redhat.com> - 0.7-1
- 0.7 bump
- Now includes the xembed utility; as xembed has no implicit support for
  config.def, this release doesn't include xembed customization via the user
  subpackage; however, this could be improved in the future
- Adding a temporary workaround for F36 builds
- SPDX migration

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 12 2016 Petr Šabata <contyk@redhat.com> - 0.6-9
- The user subpackage now properly requires redhat-rpm-config

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 17 2015 Petr Šabata <contyk@redhat.com> - 0.6-7
- Enable full RELRO
- Correct the dep list

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Petr Šabata <contyk@redhat.com> - 0.6-4
- Pass command line parameters to respective binaries in tabbed-user (#1129582)

* Wed Jun 25 2014 Petr Šabata <contyk@redhat.com> - 0.6-3
- Introduce the `user' subpackage

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 22 2014 Petr Šabata <contyk@redhat.com> - 0.6-1
- Bumping to 0.6
- Adding README and TODO to %%doc
- Dropping the unneeded constructs
- Tweaking the description a little bit

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 17 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 0.2-2
- Output is verbose now

* Sun Jan 10 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 0.2-1
- Initial package build
