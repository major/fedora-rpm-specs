%global commit ebf273bbfc52ece3bd4f341829e63c09a0555b47

Name:           python-mkdocs-macros-test
Version:        0.1.0
Release:        %autorelease
Summary:        Test macros library for the MkDocs macros plugin

License:        MIT
URL:            https://github.com/fralau/mkdocs-macros-test
Source0:        %{pypi_source mkdocs-macros-test}
# PyPI tarball doesn't include the license text and the README
Source1:        %{url}/raw/%{commit}/LICENSE.md
Source2:        %{url}/raw/%{commit}/README.md

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This is a test pluglet for mkdocs-macros. Its purpose is to serve as a template
for pluglets.}

%description %_description

%package -n     python3-mkdocs-macros-test
Summary:        %{summary}

%description -n python3-mkdocs-macros-test %_description

%prep
%autosetup -p1 -n mkdocs-macros-test-%{version}
cp -p %SOURCE1 %SOURCE2 .

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L mkdocs_macros_test

%check
%pyproject_check_import

%files -n python3-mkdocs-macros-test -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
