Name:           python-gradunwarp
Version:        1.2.1
Release:        %autorelease
Summary:        Gradient Unwarping

License:        MIT
URL:            https://github.com/Washington-University/gradunwarp
Source0:        %{url}/archive/v%{version}/gradunwarp-%{version}.tar.gz
Source1:        gradient_unwarp.1

BuildRequires:  gcc

%description
Python/Numpy package used to unwarp the distorted volumes (due to the gradient
field inhomogenities).

%package -n python3-gradunwarp
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
# used in setup.py
BuildRequires:  python3-numpy
# not mentioned in setup.py
BuildRequires:  python3-scipy
BuildRequires:  python3-nibabel
# not mentioned in setup.py
Requires:  python3-numpy
Requires:  python3-scipy
Requires:  python3-nibabel


%description -n python3-gradunwarp
Python/Numpy package used to unwarp the distorted volumes (due to the gradient
field inhomogenities).

%prep
%autosetup -n gradunwarp-%{version}
# correct version string
# remove extra compilation flags
sed -i -e "s/HCP-%{version}/%{version}/" \
    -e "s/extra_compile_args=.*)/)/" \
    setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# install script
mv %{buildroot}%{_bindir}/gradient_unwarp.py %{buildroot}%{_bindir}/gradient_unwarp
sed -i -e '1s|^.*$|#!%{__python3}|' %{buildroot}%{_bindir}/gradient_unwarp

# fix perms on .so
find %{buildroot}%{python3_sitearch}/gradunwarp/ -name '*.so' -exec chmod 755 {} \+

%pyproject_save_files gradunwarp

# install man page generated using help2man
install -m 0644 %{SOURCE1} -Dt $RPM_BUILD_ROOT/%{_mandir}/man1/

%check
%pytest

%files -n python3-gradunwarp -f %{pyproject_files}
%exclude %{python3_sitearch}/gradunwarp/core/gradient_unwarp.py
%exclude %{python3_sitearch}/gradunwarp/core/interp3_ext.c
%exclude %{python3_sitearch}/gradunwarp/core/legendre_ext.c
%exclude %{python3_sitearch}/gradunwarp/core/transform_coordinates_ext.c
%license Copying.md
%doc README.md
%{_bindir}/gradient_unwarp
%{_mandir}/man1/gradient_unwarp.*

%changelog
%autochangelog
