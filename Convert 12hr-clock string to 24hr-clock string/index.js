function timeConversion(s) {
  if (s.endsWith("PM")) {
    if (s.startsWith("12")) {
      return s.match(/\d\d\W\d\d\W\d\d/g)[0];
    }
    return s
      .replace(/^.{2}/g, (parseInt(s.match(/\d\d/g)[0]) + 12).toString())
      .match(/\d\d\W\d\d\W\d\d/g)[0];
  }
  if (s.endsWith("AM")) {
    if (s.startsWith("12")) {
      return s.replace(/^.{2}/g, "00").match(/\d\d\W\d\d\W\d\d/g)[0];
    }
    return s.match(/\d\d\W\d\d\W\d\d/g)[0];
  }
}
