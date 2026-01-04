Name:           python-esbonio
Version:        1.0.0
Release:        %autorelease
Summary:        A Language Server for Sphinx projects
License:        MIT
URL:            https://github.com/swyddfa/esbonio
Source:         %{url}/releases/download/esbonio-language-server-v%{version}/esbonio-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist websockets}
BuildRequires:  %{py3_dist sphinx}

%global _description %{expand:
Esbonio aims to make it easier to work with reStructuredText tools such as
Sphinx by providing a Language Server to enhance your editing experience.}

%description %_description

%package -n     python3-esbonio
Summary:        %{summary}

%description -n python3-esbonio %_description

%prep
%autosetup -p1 -n esbonio-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l esbonio

%check
%pyproject_check_import

%files -n python3-esbonio -f %{pyproject_files}
%{_bindir}/esbonio

%changelog
%autochangelog
