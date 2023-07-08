Name:           python-tokenize-rt
Version:        5.1.0
Release:        1%{?dist}
Summary:        Wrapper for Python's stdlib `tokenize` supporting roundtrips

License:        MIT
URL:            https://github.com/asottile/tokenize-rt
Source:         %{url}/archive/v%{version}/tokenize-rt-%{version}.tar.gz
Patch:          %{url}/commit/119b59de119361207c21dc5ee4d3ace0d1b6dff6.patch#/fix-py312-test-failures.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# Testing requirements
# covdefaults (from tox.ini -> requirements-dev.txt) is not packaged
# for Fedora, using pytest directly
BuildRequires:  python3dist(pytest)

%global _description %{expand:
The stdlib tokenize module does not properly roundtrip. This wrapper
around the stdlib provides two additional tokens ESCAPED_NL and
UNIMPORTANT_WS, and a Token data type. Use src_to_tokens and
tokens_to_src to roundtrip. This library is useful if you are writing
a refactoring tool based on the python tokenization.}

%description %_description

%package -n python3-tokenize-rt
Summary:        %{summary}

%description -n python3-tokenize-rt %_description


%prep
%autosetup -p1 -n tokenize-rt-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files tokenize_rt


%check
%pytest


%files -n python3-tokenize-rt -f %{pyproject_files}
%doc README.md
%{_bindir}/tokenize-rt


%changelog
* Thu Jul 06 2023 Maxwell G <maxwell@gtmx.me> - 5.1.0-1
- Update to 5.1.0.
- Fix Python 3.12 test failures.
- Fixes: rhbz#2220538

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 5.0.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 04 2022 Roman Inflianskas <rominf@aiven.io> - 5.0.0-1
- Update to 5.0.0 (resolve rhbz#2131856)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Roman Inflianskas <rominf@aiven.io> - 4.2.1-1
- Initial package

