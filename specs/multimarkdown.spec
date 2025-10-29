%global projectname MultiMarkdown-6

Name:           multimarkdown
# DO NOT FORGET TO CHANGE THE RELEASE !
Version:        6.7.0
Release:        %autorelease -b 8
Summary:        Lightweight markup processor to produce HTML, LaTeX, and more

# MultiMarkdown 6 is licensed under MIT, licenses of bundled software are next to the bundling declaration
# Automatically converted from old format: MIT and ((MIT and GPLv2) and zlib and BSD and MIT and BSD) - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND ((LicenseRef-Callaway-MIT AND GPL-2.0-only) AND Zlib AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD)
URL:            https://fletcher.github.io/%{projectname}/
Source0:        https://github.com/fletcher/%{projectname}/archive/%{version}/%{projectname}-%{version}.tar.gz

# UPDATED: Increase required CMake version to silence warning
Patch0:         https://github.com/fletcher/%{projectname}/commit/655c0908155758e7c94858af2fb99dc992709075.patch

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
rm -f %{buildroot}%{_bindir}/markdown %{buildroot}%{_bindir}/mmd

mkdir -p %{buildroot}%{_datadir}/doc/multimarkdown
mv %{buildroot}%{_datadir}/doc/MultiMarkdown/* %{buildroot}%{_datadir}/doc/multimarkdown

%check
# Tests disabled due to bad interactions between the toolkit and mockbuild
#ctest

%files
%license LICENSE
%{_datadir}/doc/multimarkdown/README.txt
%{_datadir}/doc/multimarkdown/LICENSE.txt
%doc QuickStart/QuickStart.*
%doc DevelopmentNotes/DevelopmentNotes.*
%{_bindir}/multimarkdown
%{_bindir}/mmd2*
%{_datadir}/texmf/tex/latex/mmd6

%changelog
%autochangelog
