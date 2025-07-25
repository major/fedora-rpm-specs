Name:           python-jaconv
Version:        0.3.4
Release:        5%{?dist}
Summary:        Pure-Python Japanese character interconverter for Hiragana, Katakana, Hankaku, Zenkaku and more

License:        MIT-0
URL:            https://github.com/ikegami-yukino/jaconv
Source:         %{url}/archive/v%{version}/jaconv-%{version}.tar.gz
# switch from nose to pytest for tests
Patch0:         https://patch-diff.githubusercontent.com/raw/ikegami-yukino/jaconv/pull/36.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
a Python Natural Language Processing (NLP) library to transliterate hiragana,
katakana and kanji (Japanese text) into rōmaji (Latin/Roman alphabet).
It can handle characters in NFC form.}

%description %_description

%package -n python3-jaconv
Summary:        %{summary}

%description -n python3-jaconv %_description


%prep
%autosetup -p1 -n jaconv-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

rm -f %{buildroot}/usr/CHANGES.rst %{buildroot}/usr/README.rst
%pyproject_save_files -l jaconv -l

%check
%pytest

%files -n python3-jaconv -f %{pyproject_files}
%doc CHANGES.rst README.rst

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 0.3.4-4
- Rebuilt for Python 3.14

* Sat Mar 22 2025 Kevin Fenzi <kevin@scrye.com> - 0.3.4-3
- Drop unneeded -t to pyproject_buildrequires. ( Fixes rhbz#2354111 )

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 30 2024 Kevin Fenzi <kevin@scrye.com> - 0.3.4-1
- Initial version
