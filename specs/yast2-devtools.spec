# Conditional for release and snapshot builds.
# Uncomment for release-builds.
%global			rel_build	1

# Conditional for bootstrapping new distributions.
# Uncomment for bootstrap-builds.
#global			bootstrap_build	1

# Settings used for build from snapshots.
%{!?rel_build:%global	commit		a85b2c6a5bf53de97883299a87f61a0bcf6844b7}
%{!?rel_build:%global	commit_date	20141215}
%{!?rel_build:%global	shortcommit	%(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global	gitver		git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global	gitrel		.git%{commit_date}.%{shortcommit}}

# Proper naming for the tarball from github.
%global			gittar		%{name}-%{version}%{!?rel_build:-%{gitver}}.tar.gz

# Place rpm-macros into proper location.
%{!?_macrosdir:%global	_macrosdir	%(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)}

# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global	_pkgdocdir	%{_docdir}/%{name}-%{version}}

# Are licenses packaged using %%license?
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
%bcond_without		license_dir
%else  # 0%%{?fedora} >= 21 || 0%%{?rhel} >= 8
%bcond_with		license_dir
%endif # 0%%{?fedora} >= 21 || 0%%{?rhel} >= 8

# This is a package from a whole suite.
%global			suite_name	yast
%global			name_suffix	devtools
%global			repo_name	%{suite_name}-%{name_suffix}
%global			src_url		https://github.com/%{suite_name}/%{repo_name}

Name:		%{suite_name}2-%{name_suffix}
Version:	3.1.36
Release:	21%{?gitrel}%{?dist}
Summary:	YaST Development Tools

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://%{suite_name}.github.io
# Sources for release-builds.
%{?rel_build:Source0:	%{src_url}/archive/%{repo_name}/master/%{version}.tar.gz#/%{gittar}}
# Sources for snapshot-builds.
%{!?rel_build:Source0:	%{src_url}/archive/%{commit}.tar.gz#/%{gittar}}

BuildArch:	noarch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:	automake
BuildRequires:	docbook-style-xsl
BuildRequires:	doxygen
BuildRequires:	fdupes
BuildRequires:	gettext
BuildRequires:	libtool
BuildRequires:	libxslt
BuildRequires:	perl-generators
BuildRequires:	pkgconfig
BuildRequires:	rubygem(redcarpet)
BuildRequires:	rubygem(yard)

Requires:	%{_bindir}/desktop-file-validate
Requires:	%{_bindir}/libtool
Requires:	%{_bindir}/xsltproc
Requires:	automake
Requires:	cmake
Requires:	docbook-style-xsl
Requires:	doxygen
Requires:	emacs-filesystem
Requires:	filesystem
Requires:	gettext
Requires:	redhat-rpm-config
Requires:	rubygem(redcarpet)
Requires:	rubygem(yard)

# Additional requirements after bootstrap.
%if 0%{?bootstrap_build} == 0
BuildRequires:	pkgconfig(%{name})
Requires:	config(yast2-filesystem)
%endif # 0%%{?bootstrap_build} == 0

%description
Common scripts and templates for developing
and building YaST2 modules and components.


%prep
%setup -qn %{repo_name}-%{?rel_build:%{repo_name}-master-%{version}}%{!?rel_build:%{commit}}

# Bootstrap autosh*t.
./build-tools/scripts/y2autoconf --bootstrap ./build-tools/
./build-tools/scripts/y2automake --bootstrap ./build-tools/
%{__cat} ./build-tools/aclocal/*.m4 > acinclude.m4
%{_bindir}/autoreconf --force --install -Wall

# Fix-up hashbangs.
for _file in $(%{__grep} -Rle '#![ \t]*/usr/bin/env' .)
do
  %{__sed} -e '1s~^#![ \t]*%{_bindir}/env[ \t]\+~#!%{_bindir}/~'	\
	< ${_file} > ${_file}.new &&					\
	/bin/touch -r ${_file} ${_file}.new &&				\
	%{__mv} -f ${_file}.new ${_file}
done

# Adjust %%yast_docdir for releases with versioned %%_docdir.
%if (0%{?fedora} && 0%{?fedora} < 21) || (0%{?rhel} && 0%{?rhel} < 8)
_file="./build-tools/rpm/macros.yast"
%{__sed} -e 's!^%%yast_docdir.*$!&-%%{version}!'			\
	< ${_file} > ${_file}.new &&					\
	/bin/touch -r ${_file} ${_file}.new &&				\
	%{__mv} -f ${_file}.new ${_file}
%endif # (0%%{?fedora} && 0%%{?fedora} < 21) || (0%%{?rhel} && 0%%{?rhel} < 8)


%build
%configure
%make_build


%install
%make_install

# Create additionally needed dirs.
%{__mkdir} -p %{buildroot}%{?_macrosdir} %{buildroot}%{?_pkgdocdir}

# Install ChangeLog.
%{__cp} -a ./package/yast2-devtools.changes				\
		%{buildroot}%{?_pkgdocdir}/ChangeLog

# Install additional tools.
%{__install} -pm 0755 ./mass-tools/y2m %{buildroot}%{_bindir}

# Move documentation to %%{?_pkgdocdir}.
%{__mv} -f %{buildroot}%{_docdir}/packages/yast2-devtools/*		\
		%{buildroot}%{?_pkgdocdir}
%{__install} -pm 0644 ./mass-tools/README				\
	%{buildroot}%{?_pkgdocdir}/README.y2m.txt

# Move rpm-macros to proper dir.
%if "0%{?_macrosdir}" != "0%{_sysconfdir}/rpm"
%{__mv} -f %{buildroot}%{_sysconfdir}/rpm/* %{buildroot}%{?_macrosdir}
%endif # "0%%{?_macrosdir}" != "0%%{_sysconfdir}/rpm"

# Final clean-up.
%{__rm} -rf %{buildroot}%{_docdir}/packages				\
%if %{with license_dir}
		%{buildroot}%{?_pkgdocdir}/COPYING			\
%endif # %%{with license_dir}
;

# Softlink duplicate files.
%fdupes -s %{buildroot}


%check
if [ ! -f "%{yast_ydatadir}/devtools/NO_MAKE_CHECK" ]; then
	%{__make} check VERBOSE=1 Y2DIR="%{buildroot}/%{yast_dir}"	\
			DESTDIR="%{buildroot}"
fi


%files
%if %{with license_dir}
%license COPYING
%endif # %%{with license_dir}
%doc %{?_pkgdocdir}
%{_bindir}/y2*
%{_datadir}/aclocal/*.m4
%{_datadir}/cmake/Modules/*.cmake
%{_datadir}/emacs/site-lisp/*
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/vim
%{_datadir}/YaST2/*
%{?_macrosdir}/macros.%{suite_name}
%{_prefix}/lib/YaST2/*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.36-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.36-20
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.36-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.36-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.36-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.36-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.36-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.36-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.36-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.36-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.36-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.36-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.36-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.36-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.36-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.36-6
- Escape macros in %%changelog

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 23 2015 Björn Esser <bjoern.esser@gmail.com> - 3.1.36-1
- new upstream release

* Wed May 13 2015 Björn Esser <bjoern.esser@gmail.com> - 3.1.34-1
- new upstream release
- added 'Requires: %%{_bindir}/desktop-file-validate', it's a
  commonly needed BuildRequires for other YaST-packages
- adjust %%yast_docdir for releases with versioned %%_docdir
- use %%{__install} for adding `y2m` to package
- improved cleaning of empty left-over dirs
- run autoreconf with `-Wall`-flag

* Tue May 12 2015 Björn Esser <bjoern.esser@gmail.com> - 3.1.33-1
- new upstream release
- dropped %%{__chmod} on `gettextdomains`, fixed in upstream's Autotools
- dropped verbosity on autoreconf-invocation
- changed %%{url} to new location

* Mon May 11 2015 Björn Esser <bjoern.esser@gmail.com> - 3.1.32-1
- new upstream release
- add `-Wobsolete`-flag to autoreconf
- remove Patch0 and Patch1, since they are merged into upstream
- use conditional and more elaborate test-invocation

* Sat May 09 2015 Björn Esser <bjoern.esser@gmail.com> - 3.1.31-2
- fix AutoTools: Obsoleted m4s found: AC_PROG_LIBTOOL (#1220036)
- add Patch0: use new `AC_INIT()`-syntax with args in square braces
- add Patch1: replace obsolete `A[CM]_PROG_LIBTOOL` with `LT_INIT()`

* Fri May 08 2015 Björn Esser <bjoern.esser@gmail.com> - 3.1.31-1
- new upstream release

* Fri May 08 2015 Björn Esser <bjoern.esser@gmail.com> - 3.1.30-1
- initial rpm release (#1218749)

* Mon May 04 2015 Björn Esser <bjoern.esser@gmail.com> - 3.1.30-0.1
- bootstrapping
