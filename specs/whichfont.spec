Name:          whichfont
Version:       2.3.0
Release:       2%{?dist}
Summary:       Querying Fontconfig

License:       GPL-3.0-or-later
URL:           https://github.com/sudipshil9862/whichfont
Source0:       %{url}/archive/refs/tags/%{version}.tar.gz#/whichfont-%{version}.tar.gz

BuildRequires: fontconfig-devel
BuildRequires: meson
BuildRequires: gcc
BuildRequires: make

%description
Querying fontconfig for certain code point. 

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check


%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jun 11 2025 Sudip Shil <sshil@redhat.com> - 2.3.0-1
- Improve input handling for -f option and Update test cases in to cover new scenarios and edge cases.
- now tests.sh can capture segmentation fault and save in test_error txt file
- Created github workflow action tests.yml in github - if test fails then it is usefull for CI and automation.

* Thu May 08 2025 Sudip Shil <sshil@redhat.com> - 2.2.0-1
- Modified input_char to handle multiple words as a single input string, allowing space-separated characters.
- :: as the delimiter for Fontconfig parameters.
- help section in better format
- Modified tests.sh to include new test cases for space-separated inputs and :: parameter handling.

* Tue Apr 15 2025 Sudip Shil <sshil@redhat.com> - 2.1.0-0
- Added --language (-l) CLI option to detect the default font for a given language code, which detects and prints the default font family that supports the specified language.
- Introduced valid_langs[] array containing known language codes supported by fontconfig, Rejects invalid language codes early with a clear error message.
- Checks not only if a font is returned, but whether it actually supports the given language.
- Updated --help output to include usage for --language option.
- updated readme with installation, build section.

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 21 2023 Sudip Shil <sshil@redhat.com> - 1.0.9-1
- printing unicode by default. no option like -u or --unicode needed from now

* Wed Sep 13 2023 Sudip Shil <sshil@redhat.com> - 1.0.8-1
- Handling non-printable charcaters
- Print nicer names for all non-printable characters
- code rendering

* Mon Sep 04 2023 Sudip Shil <sshil@redhat.com> - 1.0.7-2
- bug solved: printing wrong unicode for multiple characters

* Thu Aug 31 2023 Sudip Shil <sshil@redhat.com> - 1.0.7-1
- feature added: fontname option, sans-serif would be default
- feature added: add option to print utf8 hex sequence

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Sudip Shil <sshil@redhat.com> - 1.0.6-1
- help section changed

* Wed May 17 2023 Sudip Shil <sshil@redhat.com> - 1.0.5-2
- spec file updated

* Wed May 17 2023 Sudip Shil <sshil@redhat.com> - 1.0.5-1
- code rendering for initial packaging of whichfont in fedora 

* Wed Apr 26 2023 Sudip Shil <sshil@redhat.com> - 1.0.4-1
- introducing run.sh
- README.md updated with run.sh
- help text changes

* Wed Apr 26 2023 Sudip Shil <sshil@redhat.com> - 1.0.3-1
- more detailed --help text
- README simplify
- mix character priting in different way

* Thu Apr 20 2023 Sudip Shil <sshil@redhat.com> - 1.0.2-1
- consecusive charcater for same fontresult
- memory leak bug solved

* Mon Apr 17 2023 Sudip Shil <sshil@redhat.com> - 1.0.1-1
- -h option for help
- --all, --sort, --help long options are available
- warning will be given if no input after `whichfont -a`

* Mon Apr 17 2023 Sudip Shil <sshil@redhat.com> - 1.0.0-1
- Initial release of whichfont
