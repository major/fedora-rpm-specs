%bcond check 1

%global forgeurl https://github.com/pydicom/pynetdicom

%global _description %{expand:
pynetdicom is a pure Python package that implements the DICOM
networking protocol. Working with pydicom, it allows the easy creation of 
DICOM Service Class Users (SCUs) and Service Class Providers (SCPs).}

Name:           python-pynetdicom
Version:        2.1.1

%forgemeta

Release:        4%{?dist}
Summary:        A Python implementation of the DICOM networking protocol

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

# Downstream-only: remove the upper bound on the version of pydicom,
# specifically allowing version 3. Upstream is also working toward a release
# with pydicom 3 support; see the comment in
# https://github.com/pydicom/pynetdicom/pull/965.
Patch:          pynetdicom-2.1.1-pydicom-3.patch

BuildArch:      noarch

BuildRequires:  python3-devel

# Test dependencies; see the test extra in pyproject.toml, which also has
# unwanted coverage-analysis dependencies.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pyfakefs}
# (Also required to import some modules for “smoke tests”)
BuildRequires:  %{py3_dist sqlalchemy}
# Otherwise, pydicom test data would have to be downloaded.
BuildRequires:  %{py3_dist pydicom-data}

%description %_description

%package -n python3-pynetdicom
Summary:        %{summary}

%description -n python3-pynetdicom %_description

%package -n python3-pynetdicom-utils
Summary:        Some commands based on pynetdicom
Conflicts:      dcmtk
Requires:       python3-pynetdicom = %{version}-%{release}

%description -n python3-pynetdicom-utils
Some commands based on pynetdicom

%prep
%forgeautosetup -p1
%py3_shebang_fix .

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L pynetdicom
# pynetdicom 2.1.1 installs LICENSE file into site-packages/
# https://github.com/pydicom/pynetdicom/issues/966
rm %{buildroot}%{python3_sitelib}/LICENCE

# Remove commands already provided by dcmtk with the same name
# https://github.com/pydicom/pynetdicom/issues/968
# rm -rf %{buildroot}%{_bindir}

%check
%{pyproject_check_import \
    -e 'pynetdicom.tests*' \
    -e 'pynetdicom.apps.tests*' \
    -e 'pynetdicom.benchmarks*'}
%if %{with check}
# tests in the apps/ part not reliable, upstream advice to disable them
# https://github.com/pydicom/pynetdicom/issues/498
ignore="${ignore-} --deselect=pynetdicom/apps/tests"

# TODO: Why does this fail (even without pydicom 3.0.0)?
# >       assert self.fsm._changes[:5] == [
#             ("Sta1", "Evt1", "AE-1"),
#             ("Sta4", "Evt2", "AE-2"),
#             ("Sta5", "Evt3", "AE-3"),
#             ("Sta6", "Evt12", "AR-2"),
#             ("Sta8", "Evt16", "AA-3"),
#         ]
# E       AssertionError: assert [('Sta1', 'Evt1', 'AE-1'), ('Sta4', 'Evt2',
#         'AE-2'), ('Sta5', 'Evt3', 'AE-3'), ('Sta6', 'Evt12', 'AR-2')] ==
#         [('Sta1', 'Evt1', 'AE-1'), ('Sta4', 'Evt2', 'AE-2'), ('Sta5', 'Evt3',
#         'AE-3'), ('Sta6', 'Evt12', 'AR-2'), ('Sta8', 'Evt16', 'AA-3')]
# E
# E         Right contains one more item: ('Sta8', 'Evt16', 'AA-3')
k="${k-}${k+ and }not (TestState08 and test_evt16)"

# This fails with pydicom 3.0.0 because a deprecation warning replaces the
# expected output.
# >       assert (
#             "'dataset' is encoded as implicit VR little endian but the file "
#             "meta has a (0002,0010) Transfer Syntax UID of 'Explicit VR "
#             "Little Endian' - using 'Implicit VR Little Endian' instead"
#         ) in caplog.text
# E       assert "'dataset' is encoded as implicit VR little endian but the
#         file meta has a (0002,0010) Transfer Syntax UID of 'Explicit VR
#         Little Endian' - using 'Implicit VR Little Endian' instead" in
#         "WARNING pydicom:misc.py:82 'FileDataset.is_implicit_VR' will be
#         removed in v4.0, set the Transfer Syntax UID or use the 'implicit_vr'
#         argument with FileDataset.save_as() or dcmwrite() instead\nWARNING
#         pydicom:misc.py:82 'FileDataset.is_implicit_VR' will be removed in
#         v4.0, set the Transfer Syntax UID or use the 'implicit_vr' argument
#         with FileDataset.save_as() or dcmwrite() instead\nWARNING
#         pydicom:misc.py:82 'FileDataset.is_little_endian' will be removed in
#         v4.0, set the Transfer Syntax UID or use the 'little_endian' argument
#         with FileDataset.save_as() or dcmwrite() instead\nWARNING
#         pydicom:misc.py:82 'FileDataset.is_implicit_VR' will be removed in
#         v4.0, set the Transfer Syntax UID or use the 'implicit_vr' argument
#         with FileDataset.save_as() or dcmwrite() instead\nWARNING
#         pydicom:misc.py:82 'FileDataset.is_little_endian' will be removed in
#         v4.0, set the Transfer Syntax UID or use the 'little_endian' argument
#         with FileDataset.save_as() or dcmwrite() instead\n"
k="${k-}${k+ and }not (TestAssociationSendCStore and test_dataset_encoding_mismatch)"

# These fail with pydicom 3.0.0 due to differences in pretty-printed output, e.g.:
# _______________________ TestPrettyElement.test_seq_empty _______________________
#
# self = <pynetdicom.tests.test_dsutils.TestPrettyElement object at 0x7fc97b245270>
#
#     def test_seq_empty(self):
#         """Test empty sequence"""
#         ds = Dataset()
#         ds.EventCodeSequence = []
# >       assert (
#             "(0008,2135) SQ (Sequence with 0 items)                  # 0"
#             " EventCodeSequence"
#         ) == pretty_element(ds["EventCodeSequence"])
# E       AssertionError: assert '(0008,2135) SQ (Sequence with 0 items)                  # 0 EventCodeSequence' == '(0008,2135) SQ (Sequence with 0 item)                   # 1 EventCodeSequence'
# E
# E         - (0008,2135) SQ (Sequence with 0 item)                   # 1 EventCodeSequence
# E         ?                                                        -  ^
# E         + (0008,2135) SQ (Sequence with 0 items)                  # 0 EventCodeSequence
# E         ?                                     +                     ^
#
# pynetdicom/tests/test_dsutils.py:424: AssertionError
k="${k-}${k+ and }not (TestPrettyElement and test_seq_empty)"
k="${k-}${k+ and }not (TestPrettyElement and test_seq_vm_multi)"
k="${k-}${k+ and }not (TestPrettyDataset and test_sequence_empty)"
k="${k-}${k+ and }not (TestPrettyDataset and test_sequence_multi)"

%pytest ${ignore-} -k "${k-}" -rs -vv
%else
%endif

%files -n python3-pynetdicom -f %{pyproject_files}
%license LICENCE
%doc README.rst

%files -n python3-pynetdicom-utils
# No separate LICENSE file needed, since this depends on python3-pynetdicom
%{_bindir}/echoscp
%{_bindir}/echoscu
%{_bindir}/findscu
%{_bindir}/getscu
%{_bindir}/movescu
%{_bindir}/qrscp
%{_bindir}/storescp
%{_bindir}/storescu

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Sep 27 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.1.1-3
- Skip a new unexplained test failure
- Allow pydicom 3.0.0 (and skip a few failing tests)

* Thu Sep 19 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.1.1-2
- Stop disabling tests by default
- Use generated BuildRequires, and prune some obsolete or bogus manual ones
- Add an import-only smoke test, even when tests are disabled
- Update the License field to just "MIT"

* Thu Sep 19 2024 Alessio <alciregi AT fedoraproject DOT org> - 2.1.1-1
- Update to 2.1.1
- Split package: commands based on pynetdicom that clash with dcmtk

* Fri Sep 13 2024 Alessio <alciregi AT fedoraproject DOT org> - 2.1.0-7
- Remove commands conflicting with dcmtk

* Tue Sep 10 2024 Alessio <alciregi AT fedoraproject DOT org> - 2.1.0-6
- Fixed SPEC file

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.0-5
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2^20230720git1511488a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2^20230720git1511488a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Alessio <alciregi AT fedoraproject DOT org> - 2.0.2-2
- Fixes for Python 3.12
- Remove documentation

* Mon Nov 21 2022 Alessio <alciregi AT fedoraproject DOT org> - 2.0.2-1
- Update to 2.0.2

* Mon Dec 27 2021 Alessio <alciregi AT fedoraproject DOT org> - 2.0.0-1
- Update to 2.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 06 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.7-3
- Add fix for sphinx 4.0
- https://bugzilla.redhat.com/show_bug.cgi?id=1977627

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.7-2
- Rebuilt for Python 3.10

* Tue Apr 20 2021 Alessio <alciregi AT fedoraproject DOT org> - 1.5.7-1
- Update to 1.5.7

* Thu Jan 28 2021 Alessio <alciregi AT fedoraproject DOT org> - 1.5.6-1
- Update to 1.5.6

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Alessio <alciregi AT fedoraproject DOT org> - 1.5.5-1
- Update to 1.5.5

* Thu Dec 17 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.4-1
- Update to 1.5.4

* Mon Aug 24 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.3-2
- Re-enable test_fsm in pytest

* Mon Aug 24 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.3-1
- 1.5.3 release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 06 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.2-1
- 1.5.2 release

* Wed Jun 24 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.1-1
- 1.5.1 release

* Fri Jun 05 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.0-2
- Fixed dependecy with pydicom

* Mon Jun 01 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.0-1
- 1.5.0 release

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Alessio <alciregi AT fedoraproject DOT org> - 1.4.1-1
- Initial package
