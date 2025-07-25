# Copyright (C) 2024 Maxwell G <maxwell@gtmx.me>
# SPDX-License-Identifier: MIT
# License text: https://spdx.org/licenses/MIT

%bcond manpages 1
# Whether to build the scancode extra
%bcond scancode %[ %{defined fedora} && v"0%{?python3_version}" < v"3.14" ]
# Only run scancode tests (and install scancode at buildtime) when arch is not i386
%bcond scancode_tests %[ %{with scancode} && "%{_arch}" != "i386"]

%global forgeurl https://gitlab.com/fedora/sigs/go/go-vendor-tools
%define tag v%{version_no_tilde %{quote:%nil}}

Name:           go-vendor-tools
Version:        0.8.0
%forgemeta
Release:        2%{?dist}
Summary:        Tools for handling Go library vendoring in Fedora [SEE NOTE IN DESCRIPTION]

# BSD-3-Clause: src/go_vendor_tools/archive.py
License:        MIT AND BSD-3-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel

# Test dependencies
BuildRequires:  askalono-cli
BuildRequires:  trivy

%if %{with manpages}
BuildRequires:  scdoc
%endif

# First choice backend
Recommends:     askalono-cli
# Used by default for go_vendor_license report --autofill
Recommends:     go-vendor-tools+scancode
Recommends:     go-vendor-tools+all


%global common_description %{expand:
go-vendor-tools provides tools and macros for handling Go library vendoring in
Fedora.

STABILITY NOTE:

go-vendor-tools is under active development and available in the stable Fedora
and Fedora EPEL repos for testing purposes.
Expect some breaking changes between releases.
Anyone using the `%%go_vendor_*` macros in active Fedora packages MUST join the
Fedora Golang Matrix room and Fedora Go SIG mailing list to be notified of any
major changes.}

%description %common_description


%package doc
Summary:        Documentation for go-vendor-tools
Enhances:       go-vendor-tools

%description doc %common_description


%prep
%autosetup -p1 %{forgesetupargs}


%generate_buildrequires
%pyproject_buildrequires -x all,test%{?with_scancode_tests:,scancode}


%build
%pyproject_wheel
%if %{with manpages}
./doc/man/mkman.sh
%endif

mkdir -p bash_completions fish_completions zsh_completions
for bin in go_vendor_archive go_vendor_license; do
    register-python-argcomplete --shell bash "${bin}" > "bash_completions/${bin}"
    register-python-argcomplete --shell fish "${bin}" > "fish_completions/${bin}.fish"
    # Compatibility with old argcomplete versions
    if ! (register-python-argcomplete --shell zsh "${bin}" > "zsh_completions/_${bin}"); then
        echo "#compdef ${bin}" > "zsh_completions/_${bin}"
        echo -e "autoload -Uz bashcompinit\nbashcompinit" > "zsh_completions/_${bin}"
        cat "bash_completions/${bin}" >> "zsh_completions/_${bin}"
    fi
done


%install
%pyproject_install
# TODO(anyone): Use -l flag once supported by EL 9.
%pyproject_save_files go_vendor_tools

# Install RPM macros
install -Dpm 0644 rpm/macros.go_vendor_tools -t %{buildroot}%{_rpmmacrodir}

# Install documentation
mkdir -p %{buildroot}%{_docdir}/go-vendor-tools-doc
cp -rL doc/* %{buildroot}%{_docdir}/go-vendor-tools-doc

# Install manpages
%if %{with manpages}
install -Dpm 0644 doc/man/*.1 -t %{buildroot}%{_mandir}/man1/
install -Dpm 0644 doc/man/*.5 -t %{buildroot}%{_mandir}/man5/
%endif

# Install completions
install -Dpm 0644 bash_completions/* -t %{buildroot}%{bash_completions_dir}/
install -Dpm 0644 fish_completions/* -t %{buildroot}%{fish_completions_dir}/
install -Dpm 0644 zsh_completions/* -t %{buildroot}%{zsh_completions_dir}/


%check
export MACRO_DIR=%{buildroot}%{_rpmmacrodir}
%pytest


%files -f %{pyproject_files}
# Install top-level markdown files
%doc *.md
%license LICENSES/*
%{_bindir}/go_vendor*
%{bash_completions_dir}/go_vendor_*
%{fish_completions_dir}/go_vendor_*.fish
%{zsh_completions_dir}/_go_vendor_*
%{_rpmmacrodir}/macros.go_vendor_tools
%if %{with manpages}
%{_mandir}/man1/go*.1*
%{_mandir}/man5/go*.5*
%endif

%files doc
%doc %{_docdir}/go-vendor-tools-doc/

%pyproject_extras_subpkg -n go-vendor-tools all %{?with_scancode:scancode}

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jul 17 2025 Maxwell G <maxwell@gtmx.me> - 0.8.0-1
- Update to 0.8.0.

* Tue Jun 10 2025 Maxwell G <maxwell@gtmx.me> - 0.7.0-2
- Disable scancode on Python 3.14

* Sun Mar 23 2025 Maxwell G <maxwell@gtmx.me> - 0.7.0-1
- Update to 0.7.0.

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Maxwell G <maxwell@gtmx.me> - 0.6.0-1
- Update to 0.6.0.

* Mon Aug 5 2024 Maxwell G <maxwell@gtmx.me> - 0.5.1-4
- Add note about project stability to description

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 14 2024 Maxwell G <maxwell@gtmx.me> - 0.5.1-2
- Rebuild for Python 3.13

* Fri Apr 12 2024 Maxwell G <maxwell@gtmx.me> - 0.5.1-1
- Update to 0.5.1.

* Wed Apr 3 2024 Maxwell G <maxwell@gtmx.me> - 0.3.0-3
- Fix directory ownership patch

* Wed Apr 3 2024 Maxwell G <maxwell@gtmx.me> - 0.3.0-2
- Backport patch to fix directory ownership for %%go_vendor_license_install filelist

* Thu Mar 28 2024 Maxwell G <maxwell@gtmx.me> - 0.3.0-1
- Initial package (rhbz#2268011).
