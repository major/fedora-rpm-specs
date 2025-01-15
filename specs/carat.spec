# Get post-release bug fixes
%global commit      fd0b757974c491203e050912c09ac0bd504c7700
%global date        20211018
%global forgeurl    https://github.com/lbfm-rwth/carat

Name:           carat
Epoch:          1
Version:        2.1
Summary:        Crystallographic AlgoRithms And Tables

%forgemeta

Release:        6%{?dist}
License:        GPL-2.0-or-later
URL:            https://lbfm-rwth.github.io/carat/
VCS:            git:%{forgeurl}.git
Source0:        %{forgesource}
Source1:        %{name}.module.in
# Fix 2 use-after-free situations
# https://github.com/lbfm-rwth/carat/pull/107
Patch:          %{name}-use-after-free.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  environment(modules)
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  tex(latex)
BuildRequires:  tex(epic.sty)

Requires:       %{name}-tables = 1:%{version}-%{release}
Requires:       environment(modules)

%description
CARAT handles enumeration, construction, recognition, and comparison
problems for crystallographic groups up to dimension 6.  The name CARAT
is an acronym for Crystallographic AlgoRithms And Tables.

Due to its specialized nature and some generically named binaries, this
package uses environment modules to access its binaries.

%package tables
Summary:        Tables for CARAT binaries
BuildArch:      noarch

%description tables
Tables for CARAT binaries to consume.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later
Summary:        Documentation and examples for CARAT
BuildArch:      noarch

%description doc
Documentation and examples for CARAT.

%prep
%forgeautosetup -p1

%conf
# Don't ship XV thumbnails with the examples
rm -fr tex/examples/.xvpics

# Generate configure
./autogen.sh

%build
%configure
%make_build

# Build the documentation
cd tex
pdflatex manual
cd -

%install
# Install the binaries
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -dp bin/* %{buildroot}%{_libexecdir}/%{name}

# Install the environment-modules file
mkdir -p %{buildroot}%{_modulesdir}
sed 's#@LIBDIR@#'%{_libexecdir}/%{name}'#g;' < %{SOURCE1} \
  > %{buildroot}%{_modulesdir}/%{name}-%{_arch}
touch -r %{SOURCE1} %{buildroot}%{_modulesdir}/%{name}-%{_arch}

# Install the tables
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a tables %{buildroot}%{_datadir}/%{name}
rm %{buildroot}%{_datadir}/%{name}/tables/*.tar.gz
rm %{buildroot}%{_datadir}/%{name}/tables/lattices/{README.lattice,*.sh}
rm %{buildroot}%{_datadir}/%{name}/tables/qcatalog/*.sh
rm %{buildroot}%{_datadir}/%{name}/tables/symbol/{Makefile,README}

%check
cd tst
./run_all.sh
cd -

%files
%doc CHANGES.md README.md tex/README.short
%{_modulesdir}/%{name}-%{_arch}
%{_libexecdir}/%{name}/

%files tables
%doc tables/lattices/README.lattice
%license LICENSE
%{_datadir}/%{name}

%files doc
%doc tex/Graph tex/*.html tex/examples tex/manual.pdf tex/progs
%license LICENSE

%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 1:2.1-3
- Stop building for 32-bit x86

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 22 2022 Jerry James <loganjerry@gmail.com> - 1:2.1-1.20211018gitfd0b757
- Version 2.1 plus bug fixes from git
- Bump epoch to fix broken upgrade path
- License change from GPLv3+ to GPL-2.0-or-later
- Move manual into the doc subpackage

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1b1.2020.06.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1b1.2020.06.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1b1.2020.06.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul  1 2021 Jerry James <loganjerry@gmail.com> - 2.1b1.2020.06.04-1
- Update to latest git snapshot

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1b1.2019.12.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1b1.2019.12.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1b1.2019.12.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Jerry James <loganjerry@gmail.com> - 2.1b1.2019.12.16-1
- Update to latest git snapshot
- Change upstream's version scheme to one friendly to RPM
- The license file is now on github
- All patches have been upstreamed; drop them
- Add %%check script

* Thu Oct 31 2019 Jerry James <loganjerry@gmail.com> - 2.1b1.23.05.2019-1
- New upstream version
- New github URLs
- COPYING is not on github (https://github.com/lbfm-rwth/carat/issues/33)
- Add patches 0001 through 0006

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1b1.19.07.2008-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1b1.19.07.2008-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Jerry James <loganjerry@gmail.com> - 2.1b1.19.07.2008-11
- Move binaries to libexecdir so gap-pkg-carat can be noarch

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1b1.19.07.2008-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1b1.19.07.2008-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1b1.19.07.2008-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1b1.19.07.2008-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1b1.19.07.2008-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1b1.19.07.2008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 6 2016 Orion Poplawski <orion@cora.nwra.com> - 2.1b1.19.07.2008-4
- Require environment(modules), install into generic modulefiles location

* Sun Sep 13 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.1b1.19.07.2008-3
- Update config.guess to fix FTBFS on new arches

* Sat Jun 13 2015 Jerry James <loganjerry@gmail.com> - 2.1b1.19.07.2008-2
- Add COPYING as a license file

* Thu May 28 2015 Jerry James <loganjerry@gmail.com> - 2.1b1.19.07.2008-1
- Initial RPM
