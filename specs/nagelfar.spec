%global versionnodot 133

Name:           nagelfar
Version:        1.3.3
Release:        9%{?dist}
Summary:        Syntax checker for Tcl

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://nagelfar.sourceforge.net/
Source0:        http://downloads.sourceforge.net/nagelfar/%{name}%{versionnodot}.tar.gz

# Get auxiliary files from software-specific datadir
Patch0:         use-datadir-to-store-aux-files.patch
# Set tclsh as shebang for nagelfar.tcl script
Patch1:         tclsh-as-shebang.patch
# Add script to test Nagelfar installation
Patch2:         script-to-test-install.patch
# Add Tcl 9.0 support
Patch3:         tcl9-work.patch

BuildArch:      noarch

# tclsh needed for check step
BuildRequires:  tcl

Requires:       tcl
Requires:       tk

%description
Nagelfar is a Tcl application to read a Tcl program and provide static syntax
analysis - information regarding Tcl syntax errors like missing braces,
incomplete commands, etc. It is, moreover, extensible, with a customizable
exposed syntax database and plugins. Nagelfar has also support for doing
simple code coverage analysis.


%prep
%setup -q -n %{name}%{versionnodot}
%patch -P0
%patch -P1
%patch -P2
%patch -P3
chmod +x test_nagelfar.sh

%build


%install
mkdir -p %{buildroot}%{_datadir}/%{name}/
mv nagelfar.syntax %{buildroot}%{_datadir}/%{name}/
mv packagedb %{buildroot}%{_datadir}/%{name}/
mv syntaxbuild.tcl %{buildroot}%{_datadir}/%{name}/
mv syntaxdb86.tcl %{buildroot}%{_datadir}/%{name}/
mv syntaxdb87.tcl %{buildroot}%{_datadir}/%{name}/
mv syntaxdb90.tcl %{buildroot}%{_datadir}/%{name}/
# default syntaxdb points to current Tcl version (9.0)
ln -s syntaxdb90.tcl %{buildroot}%{_datadir}/%{name}/syntaxdb.tcl

mkdir -p %{buildroot}%{_bindir}
mv nagelfar.tcl %{buildroot}%{_bindir}/

mv {doc/,}call-by-name.txt
mv {doc/,}codecoverage.txt
mv {doc/,}inlinecomments.txt
mv {doc/,}messages.txt
mv {doc/,}oo.txt
mv {doc/,}plugins.txt
mv {doc/,}README.txt
mv {doc/,}syntaxdatabases.txt
mv {doc/,}syntaxtokens.txt


%check
./test_nagelfar.sh %{buildroot}%{_bindir}/nagelfar.tcl\
    %{buildroot}%{_datadir}/%{name}/syntaxdb.tcl\
    misctests/test.tcl


%files
%license COPYING
%doc call-by-name.txt codecoverage.txt inlinecomments.txt messages.txt oo.txt plugins.txt README.txt syntaxdatabases.txt syntaxtokens.txt
%{_bindir}/nagelfar.tcl
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/nagelfar.syntax
%{_datadir}/%{name}/syntaxbuild.tcl
%{_datadir}/%{name}/syntaxdb86.tcl
%{_datadir}/%{name}/syntaxdb87.tcl
%{_datadir}/%{name}/syntaxdb90.tcl
%{_datadir}/%{name}/syntaxdb.tcl
%dir %{_datadir}/%{name}/packagedb
%{_datadir}/%{name}/packagedb/*


%changelog
* Sat Jan 25 2025 Xavier Delaruelle <xavier.delaruelle@cea.fr> - 1.3.3-9
- Add patch that drops Tcl 8.5 and adds Tcl 9.0 support (patch extracted from
  upstream commits)
- Rebuilt for Tcl 9.0 (#2337734)

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.3-7
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 28 2022 Xavier Delaruelle <xavier.delaruelle@cea.fr> - 1.3.3-1
- Update to 1.3.3 (#2106590)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Xavier Delaruelle <xavier.delaruelle@cea.fr> - 1.3.2-1
- Initial package for version 1.3.2
