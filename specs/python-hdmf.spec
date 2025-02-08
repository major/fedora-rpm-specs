# XXX: note for maintainers
# Do NOT update HDMF without checking if packages that depend on it, for
# example python-pynwb can be installed with the new version

%bcond tests 1

# Not yet packaged:
#   https://pypi.org/project/linkml-runtime/
#   https://pypi.org/project/schemasheets/
#   https://pypi.org/project/oaklib/
%bcond termset 0
# [Feature]: Support zarr-python v3
# https://github.com/hdmf-dev/hdmf-zarr/issues/202
# Incompatible with Zarr 3
# https://bugzilla.redhat.com/show_bug.cgi?id=2338926
%bcond zarr 1

%global desc %{expand:
The Hierarchical Data Modeling Framework, or *HDMF* is a Python package
for working with hierarchical data. It provides APIs for specifying
data models, reading and writing data to different storage backends,
and representing data with Python object.

Documentation of HDMF can be found at https://hdmf.readthedocs.io}

# We have unbundled hdmf-common-schema. It’s possible that some version skew
# could be tolerated here, but it’s best if the unbundled version can match the
# version that was bundled in the current python-hdmf release. That version
# number can be read from
# src/hdmf/common/hdmf-common-schema/common/namespace.yaml, in
# ['namespaces'][0]['version'].
%global schema_version 1.8.0

Name:           python-hdmf
Version:        4.0.0
Release:        %autorelease
Summary:        A package for standardizing hierarchical object data

%global forgeurl https://github.com/hdmf-dev/hdmf
%global tag %{version}
%forgemeta

License:        BSD-3-Clause-LBNL
URL:            %forgeurl
Source0:        %forgesource
# Man page hand-written for Fedora in groff_man(7) format based on help output
Source1:        validate_hdmf_spec.1

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
# See the "test" extra; but since it contains linters, coverage analysis tools,
# etc. that are unwanted under
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters,
# we list test dependencies manually.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist python-dateutil}
%endif

%description %{desc}

%package -n python3-hdmf
Summary:        %{summary}

# Unbundled
%global schema_epoch 1
BuildRequires:  hdmf-common-schema = %{schema_epoch}:%{schema_version}
Requires:       hdmf-common-schema = %{schema_epoch}:%{schema_version}
%if %{without zarr}
# The zarr extra was removed in 1.14.2; we patched it back in for compatibility
# in F39/F40, but it is gone in F41, so we must Obsolete it. This can be
# removed in F44 (three releases later).
Obsoletes:      python3-hdmf+zarr < 1.14.2-1
%endif

%description -n python3-hdmf %{desc}

%pyproject_extras_subpkg -n python3-hdmf tqdm %{?with_zarr:zarr} sparse %{?with_termset:termset}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement/#_scriptlet_to_replace_a_directory
%pretrans -p <lua> -n python3-hdmf
path = "%{python3_sitelib}/hdmf/common/hdmf-common-schema"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end

%prep
%forgeautosetup -p1
rm -vrf src/hdmf/common/hdmf-common-schema/

%generate_buildrequires
%pyproject_buildrequires -x tqdm%{?with_zarr:,zarr},sparse%{?with_termset:,termset}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files hdmf

ln -s %{_datadir}/hdmf-common-schema/ \
    %{buildroot}%{python3_sitelib}/hdmf/common/hdmf-common-schema

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'

%check
%if %{with tests}
%pytest -v -rs
%endif

%files -n python3-hdmf -f %{pyproject_files}
%license license.txt
%doc README.rst Legal.txt

%{_bindir}/validate_hdmf_spec
%{_mandir}/man1/validate_hdmf_spec.1*

# symbolic link
%{python3_sitelib}/hdmf/common/hdmf-common-schema

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement/#_scriptlet_to_replace_a_directory
%ghost %{python3_sitelib}/hdmf/common/hdmf-common-schema.rpmmoved

%changelog
%autochangelog
