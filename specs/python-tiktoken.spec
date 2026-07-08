Name:           python-tiktoken
Version:        0.13.0
Release:        %autorelease
Summary:        tiktoken is a fast BPE tokeniser for use with OpenAI's models
# tiktoken is MIT
#
# Statically linked deps and their licenses.
# When updating, copy the output of %%{cargo_license_summary} from the build
# log and check it still matches the License field.
#
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        %{shrink:
    MIT AND
    Apache-2.0 AND
    Unicode-DFS-2016 AND
    (Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
    }
URL:            https://pypi.org/project/tiktoken/
Source:         %{pypi_source tiktoken}

# Manually created patch for downstream crate metadata changes
# * Allow fancy-regex 0.16 for now; upstream wants 0.17, updated from 0.13 “for
#   significantly increased performance.” See:
#   https://bugzilla.redhat.com/show_bug.cgi?id=2321464
# * Update PyO3 to 0.29, fixing RUSTSEC-2026-0176 and RUSTSEC-2026-0177. See:
#   https://github.com/openai/tiktoken/pull/574
Patch:          tiktoken-fix-metadata.diff

BuildRequires:  python3-devel
BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
tiktoken is a fast BPE tokeniser for use with OpenAI's models.}


%description %_description

%package -n     python3-tiktoken
Summary:        %{summary}

%description -n python3-tiktoken %_description


%prep
%autosetup -p1 -n tiktoken-%{version}
%cargo_prep


%generate_buildrequires
%cargo_generate_buildrequires -f python
%pyproject_buildrequires


%build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l tiktoken tiktoken_ext


%check
%pyproject_check_import
# All or nearly all tests require data files downloaded from the Internet; see
# tiktoken_ext/openai_public.py. We *could* add these as additional sources,
# copy them into a directory (renaming each file to the hexadecimal SHA1 digest
# of its original URL), and set the TIKTOKEN_CACHE_DIR environment variable
# when running the tests to use these “pre-downloaded” data files. However, not
# only would this be fussy, but it means we would have to try to figure out
# what licenses, if any, apply to these data files.


%files -n python3-tiktoken -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
