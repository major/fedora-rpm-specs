%global         pypi_name    fedora-image-uploader-messages
%global         tarball_name fedora_image_uploader_messages

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        %autorelease
Summary:        AMQP messages emitted by the fedora-image-uploader package

License:        GPL-2.0-or-later

URL:            https://pypi.org/project/%{pypi_name}/
Source0:        %{pypi_source %{tarball_name} %{version}}


BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  pyproject-rpm-macros


%global _description %{expand:
AMQP messages emitted by the fedora-image-uploader package.
Consumer can use this package to validate messages against a schema.}

%description %{_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}
%description -n python3-%{pypi_name} %{_description}

%prep
%autosetup -n %{tarball_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{tarball_name}

%check
%pyproject_check_import
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
