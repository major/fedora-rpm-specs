Name:      python-simple-rlp
Version:   0.1.3
Release:   1%{?dist}
Summary:   Simple RLP (Recursive Length Prefix)

License:   MIT
URL:       https://github.com/SamuelHaidu/simple-rlp
Source0:   %{pypi_source simple-rlp}

BuildArch: noarch

BuildRequires: python3-devel

%global _description %{expand:
Encode the and decode data structures simple and fast
This module is a alternative to official Ethereum pyrlp.

The pyrlp needs 5 dependencies. This alternative is write in pure python and
don't have any dependencies. Recommended use for projects that don't need the
Ethereum tools. If you already uses the Ethereum tools uses the pyrlp.

Features:
 * Very simple usage to encode and decode lists of data
 * Very fast to encode
 * Auto serialize python objects (check supported types)
 * Templates to convert bytes in decoded objects
 * No dependencies}

%description %_description

%package -n python3-simple-rlp
Summary:       %{summary}

%description -n python3-simple-rlp %_description


%prep
%autosetup -n simple-rlp-%{version}
sed -i 's/\r$//' README.md

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files rlp


%check
# tests are not included in srcdist


%files -n python3-simple-rlp -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
* Fri Sep 16 2022 Jonny Heggheim <hegjon@gmail.com> - 0.1.3-1
- Inital packaging
