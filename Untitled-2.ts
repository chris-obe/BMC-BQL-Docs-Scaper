// Office Script: PopulateModelTemplate
// Paste into Excel Online Automate -> New Script
// Expects params object with the keys listed in the Flow mapping below.

function main(workbook: ExcelScript.Workbook, params: {
  modelName?: string,
  applicationOwner?: string,
  applicationSME?: string,
  applicationDescription?: string,
  modelPackLink?: string,
  responsibleModeller?: string,
  consumerApps?: string,
  providerApps?: string,
  modelReviewVersion?: string,
  lastReviewDate?: string,
  lastReviewComments?: string,
  lastModelReviewer?: string,
  processesPersonalData?: string,        // expect "TRUE" / "FALSE" or "Yes"/"No"
  inScopePSNDelivery?: string,
  containsPublicSectorData?: string,
  containsSensitiveData?: string,
  allowsInternalOffshoreAccess?: string,
  allows3rdPartyAccess?: string,
  inScopeSOX?: string
}) {

  // CHANGE THIS if your sheet name is different
  const sheetName = "Sheet1";
  const sheet = workbook.getWorksheet(sheetName);
  if (!sheet) throw new Error(`Worksheet "${sheetName}" not found. Update sheetName in the script.`);

  // Helper: write only if param provided (prevents stamping "undefined")
  function safeSet(address: string, value: any) {
    if (value === undefined || value === null) return;
    sheet.getRange(address).setValue(value);
  }

  // Core fields (change addresses here if your template differs)
  safeSet("B3", params.modelName);
  safeSet("B4", params.applicationOwner);
  safeSet("B5", params.applicationSME);
  safeSet("B6", params.applicationDescription);
  safeSet("B7", params.modelPackLink);
  safeSet("B8", params.responsibleModeller);

  // Dependencies
  safeSet("B10", params.consumerApps);
  safeSet("B11", params.providerApps);

  // Update history
  safeSet("B13", params.modelReviewVersion);
  safeSet("B14", params.lastReviewDate);
  safeSet("B15", params.lastReviewComments);
  safeSet("B16", params.lastModelReviewer);

  // Data Classification booleans (put the string/value provided)
  safeSet("B19", params.processesPersonalData);
  safeSet("B20", params.inScopePSNDelivery);
  safeSet("B21", params.containsPublicSectorData);
  safeSet("B22", params.containsSensitiveData);
  safeSet("B23", params.allowsInternalOffshoreAccess);
  safeSet("B24", params.allows3rdPartyAccess);
  safeSet("B25", params.inScopeSOX);

  // Small audit stamp
  const stamp = `Populated by Flow on ${new Date().toISOString()}`;
  safeSet("G1", stamp); // G1 chosen as a small metadata cell; change if needed
}
