%global srcname octave-kernel
%global srcname_ octave_kernel

Name:           python-%{srcname}
Version:        0.34.2
Release:        %autorelease
Summary:        A Jupyter kernel for Octave

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname_}
Source0:        %pypi_source %{srcname_}

BuildArch:      noarch

BuildRequires:  octave
BuildRequires:  python3-devel
BuildRequires:  xorg-x11-server-Xvfb

%global _description \
A Jupyter kernel for Octave.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

Requires:       octave

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname_}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -rx test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname_}

%check
PYTHONPATH="%{buildroot}%{python3_sitelib}" \
    JUPYTER_PATH="%{buildroot}%{_datadir}/jupyter" \
        xvfb-run -a -s "-screen 0 640x480x24" \
           %{python3} test_octave_kernel.py -v

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst
%{_datadir}/jupyter/kernels/octave

%changelog
%autochangelog
