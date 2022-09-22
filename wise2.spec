%if 0%{?epel} < 7
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}
%endif

Name:           wise2
Version:        2.4.1
Release:        15%{?dist}
Summary:        Tools for comparison of bio-polymers

## Everything is licensed under a BSD-style license except for
## the HMMer2 libraries and models directory which are GPLv2+
## see LICENSE files for details. 
License:        BSD and GPLv2+
URL:            http://www.ebi.ac.uk/~birney/%{name}/
Source0:        http://www.ebi.ac.uk/~birney/%{name}/wise%{version}.tar.gz

## Patches from Debian package. Thanks to Philipp Benner
Patch0:         %{name}-build.patch
Patch1:         %{name}-isnumber.patch
Patch2:         %{name}-glib2.patch
Patch3:         %{name}-getline.patch
Patch4:         %{name}-ld--as-needed.patch
Patch5:         %{name}-mayhem.patch

BuildRequires: make
BuildRequires: glib2-devel, gcc, perl
BuildRequires: strace
BuildRequires: pkgconfig

%description
Wise2 is a package focused on comparisons of bio-polymers, commonly DNA
sequence and protein sequence.  A strength of Wise2 is the
comparison of DNA sequence at the level of its protein
translation. This comparison allows the simultaneous prediction of
gene structure with homology based alignment.

%package doc
Summary:    Wise2 documentation
BuildArch:  noarch
%description doc
Wise2, Wise2api and Dynamite documentation files.

%package examples
Summary:    Wise2 examples
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description examples
Here are some examples that you might want to try out.  The
Wise2 executables of course should be installed before.

%prep
%setup -q -n wise%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# Remove spurious-executable-perm
chmod a-x src/external/mott/mott_api.c
chmod a-x src/external/mott/mott_api.h
chmod a-x src/external/mott/gaplib.c
chmod a-x src/external/mott/gapstat.h

## fix interpreter in examples
sed -i 's#/usr/local/bin/perl#/usr/bin/perl#' docs/gettex.pl
## fix perms 
chmod -x test_data/rrm.HMM

## pull out licenses
for i in base dynlibsrc dyc
do
    cp src/$i/LICENSE LICENSE.$i
done
cp src/models/GNULICENSE LICENSE.GPL

%build
## removed "{?_smp_mflags}", does not support parallel build
export LDFLAGS="%{__global_ldflags}"
make -C src CC=gcc \
 CFLAGS=" -c $RPM_OPT_FLAGS -pthread -D_GNU_SOURCE %(pkg-config --cflags glib-2.0) -D_POSIX_C_SOURCE=200112L" all

%install
pushd src/bin
mkdir -p $RPM_BUILD_ROOT%{_bindir}
for i in dba dnal estwise estwisedb genewise genewisedb promoterwise scanwise scanwise_server psw pswdb
do
    install -pm 755 $i $RPM_BUILD_ROOT%{_bindir} 
done
popd

# install architecture-independent data and config files
mkdir -p $RPM_BUILD_ROOT%{_datadir}/wise2
pushd wisecfg
install -pm 644 * $RPM_BUILD_ROOT%{_datadir}/wise2
popd

# install architecture-independent files to run example tests
mkdir -p $RPM_BUILD_ROOT%{_datadir}/wise2/examples
pushd test_data
install -pm 644 * $RPM_BUILD_ROOT%{_datadir}/wise2/examples
popd

# install scripts to automatically set the WISECONFIGDIR environment variable
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
echo "export WISECONFIGDIR=%{_datadir}/wise2/" > $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/wise2.sh
echo "setenv WISECONFIGDIR %{_datadir}/wise2/" > $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/wise2.csh

%check
export WISECONFIGDIR=$PWD/wisecfg
make -C src test

%files
%doc README
%license LICENSE LICENSE.base LICENSE.dynlibsrc LICENSE.dyc LICENSE.GPL
%{_bindir}/genewisedb
%{_bindir}/estwisedb
%{_bindir}/genewise
%{_bindir}/estwise
%{_bindir}/scanwise
%{_bindir}/promoterwise
%{_bindir}/pswdb
%{_bindir}/dba
%{_bindir}/psw
%{_bindir}/scanwise_server
%{_bindir}/dnal
%{_datadir}/wise2/
%config(noreplace) %{_sysconfdir}/profile.d/*

%files doc
%license LICENSE
%doc docs

%files examples
%doc test_data/README
%{_datadir}/wise2/examples/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4.1-6
- Add gcc perl BR

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 05 2015 Antonio Trande <sagitterATfedoraproject.org> - 2.4.1-1
- Update to 2.4.1
- Fix compiler flags

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.2.0-6
- Add -D_POSIX_C_SOURCE=200112L to CFLAGS as a workaround to fix FTBFS (#511627)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb  9 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.2.0-4
- rebuilt for GCC 4.3 as requested by Fedora Release Engineering

* Thu Aug 16 2007 Alex Lancaster <alexl@users.sourceforge.net> 2.2.0-3
- Clarify license as BSD and GPLv2+

* Thu Apr 12 2007 Alex Lancaster <alexl@users.sourceforge.net> 2.2.0-2
- Pass $RPM_OPT_FLAGS to compiler as per suggestion from Ralf Corsepius.

* Wed Apr 11 2007 Alex Lancaster <alexl@users.sourceforge.net> 2.2.0-1
- Initial Fedora package.
