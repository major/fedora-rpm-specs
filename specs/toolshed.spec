Name:           toolshed
Version:        20220204hga1b3c7faf452
Release:        7%{?dist}
Summary:        Cross-development toolkit for use with the Tandy Color Computer


# Automatically converted from old format: Public Domain - needs further work
License:        LicenseRef-Callaway-Public-Domain
URL:            http://sourceforge.net/projects/toolshed/
Source0:        %{name}-%{version}-noroms.tar.gz
# toolshed contains disassmbled code that we cannot ship.  Therefore we use
# this script to remove the disassmbled code before shipping it.
# Generate the Mercurial snapshot from the SourceForge repository:
# hg archive -t tgz toolshed-<date>hg<hash>.tar.gz
# Now invoke this script while in the tarball's directory:
# ./generate-tarball.sh <date>hg<hash>
Source1: generate-tarball.sh

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  fuse-devel
BuildRequires:  discount

Patch0: toolshed-version-stringify.patch
Patch1: toolshed-OS9AttrToString-param.patch


%description
ToolShed is a package of utilities to perform cross-development from
Windows, Linux or Mac OS X computers to the Tandy Color Computer and
Dragon microcomputers. Tools are included to read/write both OS-9 RBF
disk images and CoCo Disk BASIC disk images, create WAV and CAS files
and much more.


%prep
%setup -q

%patch -P0 -p1
%patch -P1 -p1

# Turn-off weird doc permissions...
chmod 0644 doc/*


%build
make %{?_smp_mflags} CFLAGS="%{optflags} \
	-fPIE -DSYSV -Dunix -DUNIX -DSYSV -O3 -I. -I../../../include -Wall \
	-DTOOLSHED_VERSION=2.2 -D_FILE_OFFSET_BITS=64 -Wno-unused-result -Werror" \
        -C build/unix


%install
mkdir -p %{buildroot}%{_bindir}
make %{?_smp_mflags} -C build/unix install INSTALLDIR=%{buildroot}%{_bindir} DOCDIR=%{buildroot}%{_docdir}/%{name}


%files
%{_bindir}/*
%{_docdir}/%{name}/ToolShed.html


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20220204hga1b3c7faf452-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20220204hga1b3c7faf452-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20220204hga1b3c7faf452-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20220204hga1b3c7faf452-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20220204hga1b3c7faf452-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20220204hga1b3c7faf452-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 04 2022 John W. Linville <linville@tuxdriver.com> 20220204hga1b3c7faf452-1
- Update source snapshot from current upstream
- Add small fixes to correct FTBFS situation

* Thu Jan 27 2022 John W. Linville <linville@tuxdriver.com> 20180731hg6906ea14f8f5-9
- Add -fPIE to CFLAGS definition in build section

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20180731hg6906ea14f8f5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20180731hg6906ea14f8f5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20180731hg6906ea14f8f5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20180731hg6906ea14f8f5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20180731hg6906ea14f8f5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180731hg6906ea14f8f5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180731hg6906ea14f8f5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 02 2018 John W. Linville <linville@tuxdriver.com> 20180731hg6906ea14f8f5-2
- Add BuildRequires for discount to handle markdown sources

* Tue Jul 31 2018 John W. Linville <linville@tuxdriver.com> 20180731hg6906ea14f8f5-1
- Update from current upstream

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20150416hg6f0dcb7087fe-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20150416hg6f0dcb7087fe-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150416hg6f0dcb7087fe-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150416hg6f0dcb7087fe-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150416hg6f0dcb7087fe-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20150416hg6f0dcb7087fe-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20150416hg6f0dcb7087fe-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 16 2015 John W. Linville <linville@tuxdriver.com> 20150416hg6f0dcb7087fe-1
- Initial import
