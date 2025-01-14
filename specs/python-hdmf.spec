# XXX: note for maintainers
# Do NOT update HDMF without checking if packages that depend on it, for
# example python-pynwb can be installed with the new version

%bcond tests 1

# Not yet packaged:
#   https://pypi.org/project/linkml-runtime/
#   https://pypi.org/project/schemasheets/
#   https://pypi.org/project/oaklib/
%bcond termset 0

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
Version:        3.14.6
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
BuildRequires:  python3dist(pytest)
# Enables an optional integration test with this library:
BuildRequires:  python3dist(tqdm)
%endif
%if 0%{?fc40}
# The zarr extra was removed in 1.14.2, but we patched it back in; see %%prep.
BuildRequires:  tomcli
%endif
# This enables some optional tests.
BuildRequires:  %{py3_dist zarr}

%description %{desc}

%package -n python3-hdmf
Summary:        %{summary}

# Unbundled
%global schema_epoch 1
BuildRequires:  hdmf-common-schema = %{schema_epoch}:%{schema_version}
Requires:       hdmf-common-schema = %{schema_epoch}:%{schema_version}
%if !0%{?fc40}
# The zarr extra was removed in 1.14.2; we patched it back in for compatibility
# in F39/F40, but it is gone in F41, so we must Obsolete it. This can be
# removed in F44 (three releases later).
Obsoletes:      python3-hdmf+zarr < 1.14.2-1
%endif

%description -n python3-hdmf %{desc}

%pyproject_extras_subpkg -n python3-hdmf tqdm %{?with_termset:termset}
%if 0%{?fc40}
# The zarr extra was removed in 1.14.2, but we patched it back in; see %%prep.
%pyproject_extras_subpkg -n python3-hdmf zarr
%endif

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

%if 0%{?fc40}
# The zarr extra was removed in 1.14.2, via
# https://github.com/hdmf-dev/hdmf/commit/539ecf47ad1ad70e23666f7a7d750d2d84535632,
# which removed the extra and made the zarr dependency mandatory, and then
# https://github.com/hdmf-dev/hdmf/commit/62edbe44892d10d199393eae3f6c7645a2689ea4,
# which removed the mandatory dependency and just made the relevant tests
# enable themselves if zarr was present.  We want to continue to deliver 1.14.x
# bugfix updates without this minor breaking change (which upstream probably
# did not consider breaking), so we restore the extra for stable releases.
tomcli set pyproject.toml lists str \
    project.optional-dependencies.zarr 'zarr>=2.12.0'
%endif

%generate_buildrequires
%pyproject_buildrequires -x tqdm%{?with_termset:,termset}
%if 0%{?fc40}
# The zarr extra was removed in 1.14.2, but we patched it back in; see %%prep.
%pyproject_buildrequires -x zarr
%endif

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
%pytest -v
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
