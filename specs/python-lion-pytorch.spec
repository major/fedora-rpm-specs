Name:           python-lion-pytorch
Version:        0.2.3
Release:        %autorelease
Summary:        A Pytorch optimizer

License:        MIT
URL:            https://github.com/lucidrains/lion-pytorch
Source:         %{pypi_source lion_pytorch}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Lion, EvoLved Sign Momentum, new optimizer discovered by Google Brain
that is purportedly better than Adam(w), in Pytorch. This is nearly a
straight copy from here, with few minor modifications.

It is so simple, we may as well get it accessible and used asap by
everyone to train some great models, if it really works. }

%description %_description

%package -n     python3-lion-pytorch
Summary:        %{summary}

%description -n python3-lion-pytorch %_description

%prep
%autosetup -p1 -n lion_pytorch-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l lion_pytorch

%check
%pyproject_check_import

%files -n python3-lion-pytorch -f %{pyproject_files}

%changelog
%autochangelog
