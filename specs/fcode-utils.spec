%global git_commit 545fdf1faedc5fb5342a3ea44a043edde501c3eb
%global git_date 20250620

Name:		fcode-utils
Version:	1.0.3
Release:	%autorelease -s %{git_date}git%{sub %git_commit 0 7}
Summary:	Utilities for dealing with FCode
# The entire source code is GPL-2.0-only except localvalues/ and documentation/
# which are CPL-1.0 licensed
License:	GPL-2.0-only AND CPL-1.0
URL:		http://www.openfirmware.info/FCODE_suite
Source:		https://github.com/openbios/fcode-utils/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
# https://patch-diff.githubusercontent.com/raw/openbios/fcode-utils/pull/32.patch
Patch:		0001-fixes-compiling-with-gcc-15.patch
Patch:		0002-toke-add-prototypes-to-TIC-vocabulary-function-point.patch
# For tests only
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	tcsh

%description
Utilities for dealing with FCode, a Forth programming language dialect
compliant with ANS Forth.

%prep
%autosetup -p1 -n %{name}-%{git_commit}
install -p -m 0644 detok/README README.detok
install -p -m 0644 toke/README README.toke

%build
CFLAGS="%{optflags}" STRIP="/bin/true" make %{?_smp_mflags}

%install
make DESTDIR="%{buildroot}/usr" install
# Install data-files
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a localvalues $RPM_BUILD_ROOT%{_datadir}/%{name}

%check
make tests

%files
%license COPYING
%doc README README.detok README.toke documentation
%{_bindir}/detok
%{_bindir}/romheaders
%{_bindir}/toke
%{_datadir}/%{name}

%changelog
%autochangelog
