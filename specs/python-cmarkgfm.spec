Name:           python-cmarkgfm
Version:        2024.11.20
Release:        %autorelease
Summary:        Minimal bindings to GitHub's fork of cmark

License:        MIT
URL:            https://github.com/theacodes/cmarkgfm
Source:         %{pypi_source cmarkgfm}

BuildRequires:  gcc

%description
Bindings to GitHub's cmark Minimalist bindings to GitHub's fork of cmark.

%package -n     python3-cmarkgfm
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-cmarkgfm
Bindings to GitHub's cmark Minimalist bindings to GitHub's fork of cmark.

%prep
%autosetup -n cmarkgfm-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l cmarkgfm

%check
%pytest -v tests

%files -n python3-cmarkgfm -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
