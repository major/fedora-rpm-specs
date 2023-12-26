%define _lto_cflags %{nil}

Name:           wise2
Version:        2.4.1
Release:        %autorelease
Summary:        Tools for comparison of bio-polymers

## Everything is licensed under a BSD-style license except for
## the HMMer2 libraries and models directory which are GPLv2+
## see LICENSE files for details. 
License:        BSD-3-Clause AND GPL-2.0-or-later
URL:            http://www.ebi.ac.uk/~birney/%{name}/
Source0:        http://www.ebi.ac.uk/~birney/%{name}/wise%{version}.tar.gz

## Patches from Debian package. Thanks to Philipp Benner
Patch0:         %{name}-build.patch
Patch1:         %{name}-isnumber.patch
Patch2:         %{name}-glib2.patch
Patch3:         %{name}-getline.patch
Patch4:         %{name}-ld--as-needed.patch
Patch5:         %{name}-mayhem.patch
Patch6:         %{name}-c99.patch

BuildRequires:  make
BuildRequires:  glib2-devel
BuildRequires:  gcc
BuildRequires:  perl
BuildRequires:  strace

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
%autosetup -p1 -n wise%{version}

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
 CFLAGS=" -c %{build_cflags} -pthread -D_GNU_SOURCE %(pkg-config --cflags glib-2.0) -D_POSIX_C_SOURCE=200112L" all

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
%autochangelog
