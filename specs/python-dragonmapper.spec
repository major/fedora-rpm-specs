Name:           python-dragonmapper
Version:        0.3.0
Release:        %autorelease
Summary:        Identification and conversion functions for Chinese text processing

License:        MIT
URL:            https://github.com/tsroten/dragonmapper
Source:         %{url}/archive/v%{version}/dragonmapper-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Dragon Mapper is a Python library that provides identification and conversion
functions for Chinese text processing.

Features

- Convert between Chinese characters, Pinyin, Zhuyin, and the International
Phonetic Alphabet.
- Identify a string as Traditional or Simplified Chinese, Pinyin, Zhuyin, or the
International Phonetic Alphabet.}


%description %_description

%package -n     python3-dragonmapper
Summary:        %{summary}

%description -n python3-dragonmapper %_description


%prep
%autosetup -p1 -n dragonmapper-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files dragonmapper


%check
%pyproject_check_import
%pytest

%files -n python3-dragonmapper -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
