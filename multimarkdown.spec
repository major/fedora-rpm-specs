%global projectname MultiMarkdown-6

Name:           multimarkdown
Version:        6.6.0
Release:        6%{?dist}
Summary:        Lightweight markup processor to produce HTML, LaTeX, and more

# MultiMarkdown 6 is licensed under MIT, licenses of bundled software are next to the bundling declaration
License:        MIT and ((MIT and GPLv2) and zlib and BSD and MIT and BSD)
URL:            https://fletcher.github.io/%{projectname}/
Source0:        https://github.com/fletcher/%{projectname}/archive/%{version}/%{projectname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  perl

# Upstream choosed not to unbundle these:
# https://github.com/fletcher/MultiMarkdown-6/issues/180#issuecomment-584335760

# Both MIT and GPLv2 (d_string.c and d_string.h)
Provides:       bundled(multimarkdown) = 4.7.1

# The zlib/libpng License
Provides:       bundled(CuTest)

# The Revised BSD License
Provides:       bundled(argtable3)

# The MIT License
Provides:       bundled(miniz)

# The Revised BSD License
Provides:       bundled(uthash)

%description
MultiMarkdown is a superset of the Markdown lightweight markup syntax with
support for additional output formats and features.

Writing with MultiMarkdown allows you to separate the content and structure of
your document from the formatting. You focus on the actual writing, without
having to worry about making the styles of your chapter headers match, or
ensuring the proper spacing between paragraphs. And with a little forethought, a
single plain text document can easily be converted into multiple output formats
without having to rewrite the entire thing or format it by hand. Even better,
you don’t have to write in “computer-ese” to create well formatted HTML or LaTeX
commands. You just write, MultiMarkdown takes care of the rest.

%prep
%autosetup      -n %{projectname}-%{version} -S git

%build
%cmake
%cmake_build

%install
%cmake_install

# Removing these 2 files as they can cause conflicts with discount and mtools respectively:
# See https://github.com/fletcher/MultiMarkdown-6/issues/180#issuecomment-584353783
rm -f %{buildroot}/usr/bin/markdown %{buildroot}/usr/bin/mmd

# WHY ARE THOSE FILE EVEN INSTALLED THERE???
rm %{buildroot}/usr/LICENSE.txt
rm %{buildroot}/usr/README.txt

%check
%ctest

%files
%license LICENSE
%doc QuickStart/QuickStart.*
%doc DevelopmentNotes/DevelopmentNotes.*
%{_bindir}/multimarkdown
%{_bindir}/mmd2*
%{_datadir}/texmf/tex/latex/mmd6

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Lyes Saadi <fedora@lyes.eu> - 6.6.0-1
- Update to 6.6.0

* Tue Aug 04 2020 Lyes Saadi <fedora@lyes.eu> - 6.5.2-6
- Dropping Upstream's building steps and adopting instead the recommended CMake Fedora Guidelines

* Sat Aug 01 2020 Lyes Saadi <fedora@lyes.eu> - 6.5.2-5
- Fix second attempt at rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 30 2020 Lyes Saadi <fedora@lyes.eu> - 6.5.2-3
- https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 10 2020 Lyes Saadi <fedora@lyes.eu> - 6.5.2-1
- Update to 6.5.2

* Mon Feb 10 2020 Lyes Saadi <fedora@lyes.eu> - 6.5.1-4
- Patching FSF address.
- Documenting the licensing breakdown.

* Mon Feb 10 2020 Lyes Saadi <fedora@lyes.eu> - 6.5.1-3
- https://github.com/fletcher/MultiMarkdown-6/issues/180 :
- Renaming the package from MultiMarkdown-6 -> multimarkdown.

* Thu Feb 06 2020 Lyes Saadi <fedora@lyes.eu> - 6.5.1-2
- Fixing tests.

* Thu Feb 06 2020 Lyes Saadi <fedora@lyes.eu> - 6.5.1-1
- Initial package.
