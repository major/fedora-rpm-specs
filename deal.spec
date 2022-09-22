# Copyright (c) 2022 Garry T. Williams

Name: deal
Version: 3.1.11
Release: 7%{?dist}
Summary: Bridge Hand Generator
URL: https://github.com/gtwilliams/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Original source is at:
# https://bridge.thomasoandrews.com/deal/deal319.zip

# The source in this package has been modified to build without
# compiler errors.  It was also modified to find certain files in the
# installation directory instead of looking in the current directory.

License: GPLv2+ and GPL+ and BSD
# GPL+ applies only to ansidecl.h.  BSD applies only to random.c.
# GPLv2+ applies to all other files.  Some are marked explicitly but
# others fall under the blanket statement in the file LICENSE.

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make

BuildRequires: tcl-devel
BuildRequires: perl-podlators

Requires: tcl

%description
This program generates bridge hands.  It can be told to generate only
hands satisfying conditions like being balanced, having a range of
HCPs, controls, or other user-definable properties.  Hands can be
output in various formats, like pbn for feeding to other bridge
programs, deal itself, or split up into a file per player for
practise.  Extensible via Tcl.

%global build_data %{buildroot}%{_datadir}/%{name}
%global build_docs %{buildroot}%{_docdir}/%{name}

%prep
%autosetup

%build
touch Make.dep
%set_build_flags
%make_build DATA_DIR=%{_datadir}/%{name}/

%install
# Original source has no install target in its Makefile.  The original
# author didn't anticipate running the program from anywhere other
# than the source directory after doing a make command.  Pretty crude.
# We encode the install target here:
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man6
mkdir -p %{build_data}/ex
mkdir -p %{build_docs}/html

install -p -m 0755 deal     %{buildroot}%{_bindir}
install -p -m 0644 deal.6   %{buildroot}%{_mandir}/man6
install -p -m 0644 deal.tcl %{build_data}

cp -a input     %{build_data}/
cp -a format    %{build_data}/
cp -a lib       %{build_data}/
cp -a ex        %{build_data}/
cp -a docs/html %{build_docs}/

# Dedup deal/ex and doc/deal/html/ex.  All actual files are in deal/ex
# and some files in doc/deal/html/ex are now symlinks to files in
# deal/ex.
cd %{build_docs}/html/ex ; \
for f in %{build_data}/ex/*.tcl;do \
    if [ -f %{build_docs}/html/ex/$(basename $f .tcl).txt ] && \
       cmp $f %{build_docs}/html/ex/$(basename $f .tcl).txt ; then \
        ln -fs ../../../../%{name}/ex/$(basename $f) $(basename $f .tcl).txt ; \
    fi ; \
done

%files
%{_bindir}/deal
%{_mandir}/man6/deal.6*
%{_datadir}/%{name}/
%{_docdir}/%{name}/
%license GPL LICENSE

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 26 2022 Garry T. Williams <gtwilliams@gmail.com> 3.1.11-6
- Properly dedup ex directory files.

* Sat Feb 26 2022 Garry T. Williams <gtwilliams@gmail.com> 3.1.11-5
- Correct installation of symlinks.
- Add comments in spec documenting which files are under which
  licenses.

* Mon Feb 21 2022 Garry T. Williams <gtwilliams@gmail.com> 3.1.11-4
- Remove private getopt.[ch] files and replace with C library
  versions.
- Update license tag to reflect all licenses in source code.

* Mon Feb 21 2022 Garry T. Williams <gtwilliams@gmail.com> 3.1.11-3
- Remove superfluous file copies.

* Sun Feb 20 2022 Garry T. Williams <gtwilliams@gmail.com> 3.1.11-2
- Do not overwrite compiler flags in our Makefile.

* Tue Jan 18 2022 Garry T. Williams <gtwilliams@gmail.com> 3.1.11-1
- Removed chdir() on start-up.  Now special directory names get
  prepended with installation path.
- The version is .11 because the actual code from the original source
  is really .10.  It was just named .9.

* Tue Jan 18 2022 Garry T. Williams <gtwilliams@gmail.com> 3.1.9-2
- Copied https://bridge.thomasoandrews.com/deal Web site into our
  source to fix many errors when using browser to view the files in
  docs/html.

* Mon Jan 10 2022 Garry T. Williams <gtwilliams@gmail.com> 3.1.9-1
- Initial version of the package 3.1.9-1

